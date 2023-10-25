# noinspection PyUnresolvedReferences
"""Handles connections to the URLs in a pool of threads.

>>> Connection

"""

import socket
from multiprocessing import current_process
from typing import Tuple

import requests

from logger import LOGGER

exclusions = ["localhost", "127.0.0.1", socket.gethostbyname('localhost')]


def verify_url(hyperlink: Tuple[str, str], timeout: Tuple[int, int] = (3, 3)) -> None:
    """Make a GET request to the hyperlink for validation using requests module.

    Args:
        hyperlink: Takes a tuple of the name and URL.
        timeout: A tuple of connect timeout and read timeout.

    See Also:
        - Ignores localhost URLs.
        - Ignores URLs that return 429 status code.
        - Retries once with a longer connect and read timeout in case of a timeout error.

    Raises:
        ValueError: When a particular URL is unreachable.
    """
    text, url = hyperlink
    try:
        response = requests.get(url, timeout=timeout)
        if response.ok:
            return
        if response.status_code == 429:
            LOGGER.warning("[%s] - '%s' - '%s' returned %s", current_process().name, text, url, response)
            return
    except requests.Timeout as error:
        LOGGER.warning("Timeout error: %s", error.response)
        # Retry with a longer timeout if URL times out with 3-second timeout
        return verify_url(hyperlink, (10, 10))
    except requests.RequestException as error:
        LOGGER.debug(error)
    if any(map(lambda keyword: keyword in url, exclusions)):
        LOGGER.warning("[%s] - '%s' - '%s' is broken but excluded", current_process().name, text, url)
    else:
        raise ValueError(f"[{current_process().name}] - {text!r} - {url!r} is broken")
