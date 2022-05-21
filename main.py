""" The module reads the user-defined telegram channel,
    which id it gets through the console input
    and sends the messages with photos to another defined channel.
    """
import argparse
import requests

from telethon import TelegramClient, events
from telegram import helper
from telegram import telegram

helper.logfile()
session = requests.session()

parser = argparse.ArgumentParser(description='Get connection with the telegram client')
parser.add_argument('--api_id', type=int, dest='api_id', help='Telegram api_id for the Telegram client')
parser.add_argument('--api_hash', type=str, dest='api_hash', help='Telegram api_hash for the Telegram client')
parser.add_argument('--bot_token', type=str, dest='bot_token', help='Telegram bot_token for the Telegram API')
parser.add_argument('--listening_group', type=int, dest='listening_group', help='Telegram listening_group for the '
                                                                                'Telegram client')
parser.add_argument('--target_group', type=str, dest='target_group', help='Telegram target_group for the Telegram '
                                                                          'client')
parser.add_argument('--word', type=str, dest='word', help='A word, which should be replaced in the message')
parser.add_argument('--new_word', type=str, dest='new_word', help='A new word, which should be in the message')

args = parser.parse_args()


class BasicException(Exception):
    """
    To avoid issues with Exception
    """


client = TelegramClient(
    'retranslator',
    args.api_id,
    args.api_hash
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
    if chat_id == args.listening_group:
        message = event.raw_text
        photo = event.photo
        try:
            if photo is not None and message is not None:
                file = await client.download_media(photo, file="Download")
                helper.warn(message)
                helper.warn(file)
                if args.word:
                    message = message.replace(
                        args.word,
                        args.new_word
                    )
                telegram.send_message_with_photo(
                    session,
                    args.target_group,
                    args.bot_token,
                    file,
                    message
                )
                helper.deleter(file)
            if photo is not None and message is None:
                file = await client.download_media(photo, file="Download")
                helper.warn(file)
                telegram.send_message_with_photo(
                    session,
                    args.target_group,
                    args.bot_token,
                    file)
                helper.deleter(file)
            if photo is None and message is not None:
                helper.warn(message)
                if args.word:
                    message = message.replace(
                        args.word,
                        args.new_word
                    )
                telegram.send_message(session,
                                      args.target_group,
                                      args.bot_token,
                                      message)
        except BasicException:
            helper.info(event)
            telegram.send_message(
                session,
                args.target_group,
                args.bot_token,
                f'Something went wrong: {event}'
            )


client.start()
client.run_until_disconnected()
