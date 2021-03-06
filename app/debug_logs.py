import subprocess


class Error(Exception):
    pass


class LogCollectionScriptFailedError(Error):
    pass


def collect():
    """Collects and aggregates contents of BasslineMnk-related logs and files.

    Returns:
        A large string with the full contents of BasslineMnk's debug logs and
        configuration files.
    """
    try:
        return subprocess.check_output(
            ['sudo', '/opt/basslinemnk-privileged/collect-debug-logs', '-q'])
    except subprocess.CalledProcessError as e:
        raise LogCollectionScriptFailedError(str(e)) from e
