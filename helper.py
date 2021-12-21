""" The helper module serves as an assistant to other modules."""

import json
import logging
import os


def info(message: str):
    """
    :param message:
    This function defines logging parameters for information purposes.
    The object to be logged must be passed as input.
    """
    logging.basicConfig(
        format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
        level=logging.INFO
    )
    logging.info(message)


def warn(message: str):
    """
    :param message:
    This function defines logging parameters for warnings.
    The object to be logged must be passed as input.
    :return: None
    """
    logging.basicConfig(
        format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
        level=logging.WARNING
    )
    logging.warning(message)


def logfile():
    """This function defines parameters for
    debugging logging and subsequent writing to a file."""
    if not os.path.exists('logs'):
        os.makedirs('logs')
    logging.basicConfig(
        filename="logs/log.txt",
        filemode='a',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG
    )


def deleter(path: str):
    """
    :param path:
    This function is used to delete photos
    that are saved in the "Download" folder.
    It takes a string with the path
    to the file such as
    'Download/name_of_the_file.jpg'.
    """
    try:
        os.remove(path)
        warn(f'The file {path} was deleted')
    except OSError as some_error:
        print(f'Error: {path} : {some_error.strerror}')
