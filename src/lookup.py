# noinspection PyUnresolvedReferences
"""Handles lookup for hyperlinks in markdown files using regex search.

>>> Lookup

See Also:
    - ``INLINE_LINK_RE`` is a regular expression for matching inline links in the format [text](URL).
    - ``FOOTNOTE_LINK_TEXT_RE`` is a regular expression for matching footnote links in the format [text][number].
    - ``FOOTNOTE_LINK_URL_RE`` is a regular expression for matching footnote URLs in the format [number]: URL.
    - ``ANCHORED_LINK_RE`` is a regular expression for matching anchored links in the format [text]: URL.
"""

import re
from collections.abc import Generator
from typing import Tuple

INLINE_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')  # noqa: RegExpRedundantEscape
FOOTNOTE_LINK_TEXT_RE = re.compile(r'\[([^\]]+)\]\[(\d+)\]')  # noqa: RegExpRedundantEscape
FOOTNOTE_LINK_URL_RE = re.compile(r'\[(\d+)\]:\s+(\S+)')  # noqa: RegExpRedundantEscape
ANCHORED_LINK_RE = re.compile(r'\[([^\]]+)\]:\s+(\S+)')  # noqa: RegExpRedundantEscape


def find_md_links(markdown: str) -> Generator[Tuple[str, str]]:
    """Return list of tuples with hyperlinks in the markdown content.

    Args:
        markdown: Data from markdown file.

    Yields:
        Tuple[str, str]:
        Tuple of the string and the associated URL.
    """
    yield from list(INLINE_LINK_RE.findall(markdown))
    yield from list(ANCHORED_LINK_RE.findall(markdown))
    footnote_links = dict(FOOTNOTE_LINK_TEXT_RE.findall(markdown))
    footnote_urls = dict(FOOTNOTE_LINK_URL_RE.findall(markdown))
    for key in footnote_links.keys():
        yield footnote_links[key], footnote_urls[footnote_links[key]]
