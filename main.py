""" The module reads the user-defined telegram channel,
    which id it gets through the console input
    and sends the messages with photos to another defined channel.
    """
import argparse

from telethon.errors.rpcerrorlist import MediaCaptionTooLongError
from telethon import TelegramClient, events
from telegram import helper
from telegram import translator

helper.logfile()

parser = argparse.ArgumentParser(description='Get connection with the telegram client')
parser.add_argument('--name_session', type=str, dest='name_session', help='Name_session for your telegram client')
parser.add_argument('--api_id', type=int, dest='api_id', help='Telegram api_id for the Telegram client')
parser.add_argument('--api_hash', type=str, dest='api_hash', help='Telegram api_hash for the Telegram client')
parser.add_argument('--listening_group', type=int, dest='listening_group',
                    help='Telegram listening_group for the '
                         'Telegram client')
parser.add_argument('--target_group', type=int, dest='target_group', help='Telegram target_group for the Telegram '
                                                                          'client')
parser.add_argument('--word', type=str, dest='word', help='A word, which should be replaced in the message')
parser.add_argument('--new_word', type=str, dest='new_word', help='A new word, which should be in the message')
parser.add_argument('--key', type=str, dest='key', help='auth-key, to translate texts')

args = parser.parse_args()

client = TelegramClient(
    args.name_session,
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
        chat = await client.get_entity(event.chat_id)
        if args.key:
            message = await translator.translate(args.key, target_lang="RU", text=message, source_lang="EN")
        if args.word:
            message = message.replace(args.word, args.new_word)
        if event.media:
            helper.creator("media")
            temporary_file = await client.download_media(event.media, file="media")
            helper.logging.info(f"{chat.title}: New media - {temporary_file}")
            try:
                await client.send_message(args.target_group, message=message, file=temporary_file)
            except MediaCaptionTooLongError:
                helper.logging.info(f"Exception thrown when sending a message: {MediaCaptionTooLongError}")
                await client.send_file(args.target_group, file=temporary_file)
                await client.send_message(args.target_group, message)
            helper.deleter(temporary_file)
        elif message and not (event.file or event.video or event.photo):
            helper.logging.info(f"{chat.title}: New message - {message}")
            await client.send_message(args.target_group, message)


client.start()
client.run_until_disconnected()
