# noinspection PyUnresolvedReferences
"""Configures a Python logger with a stream handler.

>>> Logger

See Also:
    - This is a customized logger allowing log messages to be displayed in the console.
    - Logger includes information about the log level, function name, and line number.
"""

import logging

LOGGER = logging.getLogger(__name__)
DEFAULT_LOG_FORM = '%(levelname)-8s [%(funcName)s:%(lineno)d] - %(message)s'
DEFAULT_FORMATTER = logging.Formatter(datefmt='%b-%d-%Y %I:%M:%S %p', fmt=DEFAULT_LOG_FORM)
HANDLER = logging.StreamHandler()
HANDLER.setFormatter(fmt=DEFAULT_FORMATTER)
LOGGER.addHandler(hdlr=HANDLER)
