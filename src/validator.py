import logging
import os
import pathlib
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import Process, current_process

from src import lookup, connection, git
from src.logger import LOGGER

OWNER = sys.argv[1]
REPO = sys.argv[2]
FAIL = sys.argv[3]
DEBUG = sys.argv[4]
if DEBUG == "true":
    LOGGER.setLevel(level=logging.DEBUG)
else:
    LOGGER.setLevel(level=logging.INFO)


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
        for iterator in lookup.find_md_links(md_file):
            # noinspection PyTypeChecker
            future = executor.submit(connection.verify_url, iterator)
            futures[future] = iterator
    try:
        file = current_process().name.split('.-')[1]
    except IndexError:
        file = current_process().name
    LOGGER.info("Hyperlinks validated in '%s': %d", file, len(futures))
    for future in as_completed(futures):
        if future.exception():
            LOGGER.error(future.exception())
            sys.exit(1)


def check_all_md_files() -> None:
    """Downloads all the markdown files from wiki and initiates individual validation process for each markdown file."""
    _set_exit_code = False
    # Scans markdown files locally
    md_files = [os.path.join(__path, file_) for __path, __directory, __file in os.walk(os.getcwd())
                for file_ in __file if file_.lower().endswith(".md")]
    LOGGER.debug(md_files)

    # Checks markdown files in repo
    processes = []
    for file in md_files:
        proc = Process(target=verify_hyperlinks_in_md, args=(file,))
        proc.start()
        proc.name = file
        processes.append(proc)

    # Clones wiki pages
    wiki_path = f"{REPO}.wiki"
    if all((REPO, OWNER)) and git.run_command(f"git clone https://github.com/{OWNER}/{wiki_path}.git"):
        wiki_path = os.path.join(os.getcwd(), wiki_path)
        if os.path.isdir(wiki_path):
            for file in os.listdir(wiki_path):
                if file.endswith(".md"):
                    process = Process(target=verify_hyperlinks_in_md, args=(os.path.join(wiki_path, file),))
                    process.start()
                    process.name = file
                    processes.append(process)
        else:
            LOGGER.info("Clone ran successfully but wiki path wasn't found")
            _set_exit_code = True

    for process in processes:
        process.join()
        if process.exitcode != 0:
            LOGGER.error("Process '%s' exited with a non-zero exit code.", process.name)
            _set_exit_code = True

    if FAIL == "true" and _set_exit_code:
        LOGGER.exception("Setting exit code to 1")
        sys.exit(1)
    elif _set_exit_code:
        LOGGER.exception("Setting exit code to 0, although there were errors")
        sys.exit(0)


if __name__ == '__main__':
    check_all_md_files()
