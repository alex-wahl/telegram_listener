""" The module reads the user-defined telegram channel,
    which id it gets through the console input
    and sends the messages with photos to another defined channel.
    """

import requests
from telethon import TelegramClient, events
import helper
import telegram
from cmd_line_setup_parser import parse_setup_options_from_cmd

helper.logfile()
session = requests.session()

setup_params = parse_setup_options_from_cmd()
bot_token = setup_params['bot_token']
target_group = setup_params['target_group_id'] \
    if 'target_group_id' in setup_params else setup_params['target_group']


class BasicException(Exception):
    """
    To avoid issues with Exception
    """


client = TelegramClient(
    'retranslator',
    setup_params['client_api_id'],
    setup_params['client_api_hash']
)


@client.on(events.NewMessage)
async def sender(event):
    """
    This method listens to a given channel or group
    on telegram via its chat_id and then
    when a new event occurs as a message or photo,
    copies it and sends it to the telegram bot,
    which then sends it to the given channels.
    """
    chat_id = event.chat_id
    if chat_id == setup_params['listening_group']:
        message = event.raw_text
        photo = event.photo
        try:
            if photo is not None and message is not None:
                file = await client.download_media(photo, file="Download")
                helper.warn(message)
                helper.warn(file)
                if "replace" in setup_params:
                    message = message.replace(
                        setup_params['replace'],
                        setup_params['text']
                    )
                telegram.send_message_with_photo(
                    session,
                    target_group,
                    bot_token,
                    file,
                    message
                )
                helper.deleter(file)
            if photo is not None and message is None:
                file = await client.download_media(photo, file="Download")
                helper.warn(file)
                telegram.send_message_with_photo(
                    session,
                    target_group,
                    bot_token,
                    file)
                helper.deleter(file)
            if photo is None and message is not None:
                helper.warn(message)
                if "replace" in setup_params:
                    message = message.replace(
                        setup_params['replace'],
                        setup_params['text']
                    )
                telegram.send_message(session,
                                      target_group,
                                      bot_token,
                                      message)
        except BasicException:
            helper.info(event)
            telegram.send_message(
                session,
                target_group,
                bot_token,
                f'Something went wrong: {event}'
            )


client.start()
client.run_until_disconnected()
