"""This module is used to send messages as well as messages
    with pictures to a specified Telegram group."""
import requests
import helper

BASE_URL = "https://api.telegram.org/bot"


def send_message_with_photo(session: requests,  # type: ignore
                            chat_id: int,
                            bot_token: str,
                            file: str,
                            message=None):
    """
    :param session:
    :param chat_id:
    :param bot_token:
    :param file:
    :param message:
    :return: object response
    """
    with open(file, 'rb') as file_for_send:
        data = {
            "chat_id": chat_id,
            "caption": message
        }
        files = {
            "photo": file_for_send,
        }
        response = session.post(BASE_URL +  # type: ignore
                                bot_token +
                                "/sendPhoto",
                                params=data,
                                files=files)
        helper.warn(
            f'send_message_with_photo request returned: {response.text}'
        )
        return response


def send_message(session: requests,  # type: ignore
                 chat_id: int,
                 bot_token: str,
                 message: str):
    """
    :param session:
    :param chat_id:
    :param bot_token:
    :param message:
    :return: object response
    """
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = session.post(BASE_URL +  # type: ignore
                            bot_token +
                            "/sendMessage",
                            params=data)
    helper.warn(f'send_message request returned: {response.text}')
    return response
