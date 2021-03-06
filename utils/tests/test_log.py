import os
import shutil

from utils import log

# --------------------------------------------------------------------------- #
# Parameters

TMP_DIR = "tmp"
EXPECTED_LOGS = [
    "[DEBUG] {} - debug",
    "[INFO] {} - info",
    "[WARNING] {} - warning",
    "[ERROR] {} - error",
    "[CRITICAL] {} - fatal",
]


def log_levels(logger):
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.fatal("fatal")


# --------------------------------------------------------------------------- #
# Setup / Teardown

def setup_function(function):
    if os.path.exists(TMP_DIR):
        shutil.rmtree("tmp")


def teardown_function(function):
    if os.path.exists(TMP_DIR):
        shutil.rmtree("tmp")


# --------------------------------------------------------------------------- #
# Tests

def test_create_logger():
    path1 = os.path.join(TMP_DIR, "1.log")
    path2 = os.path.join(TMP_DIR, "2.log")

    log1 = log.create_logger("LogOne", lvl="DEBUG", path=path1)
    log2 = log.create_logger("LogTwo", lvl="INFO", path=path2)
    log3 = log.create_logger("LogThree", lvl="ERROR", path=path2)

    log_levels(log1)
    log_levels(log2)
    log_levels(log3)

    with open(path1) as file1:
        lines = file1.readlines()
        assert len(lines) == len(EXPECTED_LOGS)
        for line, expected_log in zip(lines, EXPECTED_LOGS):
            assert expected_log.format("LogOne") in line

    with open(path2) as file2:
        lines = file2.readlines()
        assert len(lines) == 4 + 2
        for line, expected_log in zip(lines[:4], EXPECTED_LOGS[-4:]):
            assert expected_log.format("LogTwo") in line
        for line, expected_log in zip(lines[4:], EXPECTED_LOGS[-2:]):
            assert expected_log.format("LogThree") in line


def test_logclass():
    instance = log.LogClass(name="test", loglvl="INFO")

    assert instance.get_loglvl(explicit=True) == "INFO"
    instance.set_loglvl("ERROR")
    assert instance.get_loglvl(explicit=True) == "ERROR"
    instance.set_loglvl("DEBUG")
    assert instance.get_loglvl(explicit=True) == "DEBUG"
    assert instance.get_loglvl() == 10
