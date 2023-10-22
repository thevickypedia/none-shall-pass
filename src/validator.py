import logging
import os
import pathlib
import re
import socket
import subprocess
import sys
from collections.abc import Generator
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import Process, current_process
from typing import Tuple, List, Union
from urllib import request
from urllib.error import URLError

LOGGER = logging.getLogger(__name__)
DEFAULT_LOG_FORM = '%(levelname)-8s %(message)s'
DEFAULT_FORMATTER = logging.Formatter(datefmt='%b-%d-%Y %I:%M:%S %p', fmt=DEFAULT_LOG_FORM)
HANDLER = logging.StreamHandler()
HANDLER.setFormatter(fmt=DEFAULT_FORMATTER)
LOGGER.addHandler(hdlr=HANDLER)
LOGGER.setLevel(level=logging.INFO)

INLINE_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')  # noqa: RegExpRedundantEscape
FOOTNOTE_LINK_TEXT_RE = re.compile(r'\[([^\]]+)\]\[(\d+)\]')  # noqa: RegExpRedundantEscape
FOOTNOTE_LINK_URL_RE = re.compile(r'\[(\d+)\]:\s+(\S+)')  # noqa: RegExpRedundantEscape
ANCHORED_LINK_RE = re.compile(r'\[([^\]]+)\]:\s+(\S+)')  # noqa: RegExpRedundantEscape

GIT_ENV = os.environ.get("GITHUB_ENV", "sample.env")
OWNER = sys.argv[1]
REPO = sys.argv[2]


def find_md_links(markdown: str) -> Generator[Tuple[str, str]]:
    """Return list of tuples with hyperlinks in the markdown content.

    Args:
        markdown: Data from markdown file.

    Yields:
        Tuple of the string and the associated URL.
    """
    yield from list(INLINE_LINK_RE.findall(markdown))
    yield from list(ANCHORED_LINK_RE.findall(markdown))
    footnote_links = dict(FOOTNOTE_LINK_TEXT_RE.findall(markdown))
    footnote_urls = dict(FOOTNOTE_LINK_URL_RE.findall(markdown))
    for key in footnote_links.keys():
        yield footnote_links[key], footnote_urls[footnote_links[key]]


def verify_url(hyperlink: Tuple[str, str], timeout: int = 3) -> None:
    """Make a GET request to the hyperlink for validation using urllib.

    Args:
        hyperlink: Takes a tuple of the name and URL.
        timeout: A tuple of connect timeout and read timeout.

    See Also:
        - Ignores amazon and localhost URLs
        - Retries once with a longer connect and read timeout in case of a timeout error.

    Raises:
        ValueError: When a particular hyperlink breaks.
    """
    text, url = hyperlink
    try:
        response = request.urlopen(url, timeout=timeout)
        if response.getcode() == 200:
            return
    except URLError as error:
        if isinstance(error.reason, socket.timeout):
            LOGGER.warning("Timeout error: %s", error.reason)
            # Retry with a longer timeout if URL times out with 3-second timeout
            return verify_url(hyperlink, 10)
    except Exception as error:
        LOGGER.debug(error)
    if any(map(lambda keyword: keyword in url, ("amazon", "localhost", socket.gethostbyname('localhost')))):
        LOGGER.warning(f"[{current_process().name}] - {text!r} - {url!r} is broken")
    else:
        raise ValueError(f"[{current_process().name}] - {text!r} - {url!r} is broken")


def verify_hyperlinks_in_md(filename: str) -> None:
    """Get all hyperlinks in a markdown file and validate them in a pool of threads.

    Args:
        filename: Name of the markdown file to be validated.
    """
    current_process().name = pathlib.Path(filename).name
    with open(filename) as file:
        md_file = file.read()
    futures = {}
    with ThreadPoolExecutor() as executor:
        for iterator in find_md_links(md_file):
            # noinspection PyTypeChecker
            future = executor.submit(verify_url, iterator)
            futures[future] = iterator
    try:
        file = current_process().name.split('.-')[1]
    except IndexError:
        file = current_process().name
    LOGGER.info("Hyperlinks validated in '%s': %d", file, len(futures))
    for future in as_completed(futures):
        if future.exception():
            LOGGER.error(future.exception())
            if os.getenv("FAILED") == "1":
                LOGGER.info("Failed flag has been set already.")
            else:
                LOGGER.info("Setting FAILED flag to 1")
                set_exit_code()


def set_exit_code() -> None:
    """Sets the 'FAILED' env var to a non zero value."""
    env_vars = {k: v for k, v in os.environ.items()}
    env_vars['FAILED'] = 1
    with open(GIT_ENV, 'w') as env_file:
        for k, v in env_vars.items():
            env_file.write(f"{k}={v}\n")


def initiate_validation(arg: Union[str, List[str]]) -> None:
    """Verifies if filename is a string or a list and processes md validations accordingly."""
    if isinstance(arg, str):
        verify_hyperlinks_in_md(arg)
    elif isinstance(arg, list):
        for file in arg:
            verify_hyperlinks_in_md(file)
    else:
        # Should never get here
        set_exit_code()
        raise Exception("Something went wrong")


def run_git_cmd(cmd: str):
    """Run the git command."""
    try:
        subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL)
        return True
    except (subprocess.CalledProcessError, subprocess.SubprocessError, Exception) as error:
        if isinstance(error, subprocess.CalledProcessError):
            result = error.output.decode(encoding='UTF-8').strip()
            LOGGER.error(f"[{error.returncode}]: {result or error.__str__()}")
        else:
            LOGGER.error(error)


def check_all_md_files() -> None:
    """Downloads all the markdown files from wiki and initiates individual validation process for each markdown file."""
    # Scans markdown files locally
    md_files = [os.path.join(__path, file_) for __path, __directory, __file in os.walk(os.getcwd())
                for file_ in __file if file_.lower().endswith(".md")]
    LOGGER.debug(md_files)
    processes = [Process(target=initiate_validation, args=(md_files,))]
    processes[0].start()

    if not all((REPO, OWNER)):
        LOGGER.error("OWNER and REPO information not found")
        set_exit_code()
        processes[0].join()
        return

    # Clones wiki pages
    wiki_path = f"{REPO}.wiki"
    if run_git_cmd(f"git clone https://github.com/{OWNER}/{wiki_path}.git"):
        wiki_path = os.path.join(os.getcwd(), wiki_path)
    else:
        # Do not set exit code since no wiki doesn't warrant a failure
        return

    if os.path.isdir(wiki_path):
        for file in os.listdir(wiki_path):
            if file.endswith(".md"):
                process = Process(target=initiate_validation, args=(os.path.join(wiki_path, file),))
                process.start()
                processes.append(process)
    else:
        LOGGER.info("Clone ran successfully but wiki path wasn't found")
        set_exit_code()
    for process in processes:
        process.join()


if __name__ == '__main__':
    check_all_md_files()
