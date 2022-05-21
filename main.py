""" The module reads the user-defined telegram channel,
    which id it gets through the console input
    and sends the messages with photos to another defined channel.
    """
import argparse

from telethon import TelegramClient, events
from telegram import helper

helper.logfile()

parser = argparse.ArgumentParser(description='Get connection with the telegram client')
parser.add_argument('--api_id', type=int, dest='api_id', help='Telegram api_id for the Telegram client')
parser.add_argument('--api_hash', type=str, dest='api_hash', help='Telegram api_hash for the Telegram client')
parser.add_argument('--listening_group', type=int, dest='listening_group', help='Telegram listening_group for the '
                                                                                'Telegram client')
parser.add_argument('--target_group', type=int, dest='target_group', help='Telegram target_group for the Telegram '
                                                                          'client')
parser.add_argument('--word', type=str, dest='word', help='A word, which should be replaced in the message')
parser.add_argument('--new_word', type=str, dest='new_word', help='A new word, which should be in the message')

args = parser.parse_args()

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
    when a new event occurs as a message or media,
    copies it and sends it to the given channels.
    """
    chat_id = event.chat_id
    if chat_id == args.listening_group:
        message = event.raw_text
        user = await client.get_entity(event.from_id.user_id)
        chat = await client.get_entity(event.chat_id)
        if event.media:
            helper.creator("media")
            temporary_file = await client.download_media(event.media, file="media")
            await client.send_message(args.target_group, message, file=temporary_file)
            helper.logging.info(f"Message from {user.username} in chat {chat.title}. Media: {temporary_file}")
            helper.deleter(temporary_file)
        elif message and not (event.file or event.video or event.photo):
            helper.logging.info(f"Message from {user.username} in chat {chat.title}. Message: {message}")
            message = message.replace(args.word, args.new_word) if args.word else message
            await client.send_message(args.target_group, message)


client.start()
client.run_until_disconnected()
