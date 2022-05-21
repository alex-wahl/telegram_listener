""" The helper module serves as an assistant to other modules."""

import logging
import os


def creator(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def logfile():
    """This function defines parameters for
    debugging logging and subsequent writing to a file."""
    creator('logs')
    logging.basicConfig(
        filename="logs/log.txt",
        filemode='a',
        format='[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S',
        level=logging.INFO
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
        logging.info(f'The file {path} was deleted')
    except OSError as some_error:
        print(f'Error: {path} : {some_error.strerror}')
