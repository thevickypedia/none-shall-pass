# noinspection PyUnresolvedReferences
"""Runs git command using subprocess module.

>>> Git

"""

import subprocess

from logger import LOGGER


def run_command(cmd: str) -> bool:
    """Run git command to clone wiki locally and handle exceptions from subprocess module.

    Args:
        cmd: Takes the command as an argument.

    Returns:
        bool:
        A boolean flag to indicate the status.
    """
    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True, check=True)
        return True
    except (subprocess.CalledProcessError, subprocess.SubprocessError, Exception) as error:
        if hasattr(error, 'output') and error.output:
            result = error.output.decode(encoding='UTF-8').strip()
            LOGGER.warning("[%d]: %s", error.returncode, result or error.__str__())
        else:
            LOGGER.warning(error)
