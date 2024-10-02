from telethon import TelegramClient,events
from creds import *

import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

@bot.on(events.NewMessage)
async def reply(event):
    logging.info(event.raw_text)
    if event.raw_text == 'hi':
        await event.reply('Hello, This is ArjunBot!')

@bot.on(events.NewMessage(pattern='\.save'))
async def saveprof(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        sender = replied.sender
        logging.info("{} wants to save profile".format(sender.username))
        await event.reply('Saving profile...')
        await bot.download_profile_photo(sender, file='{}.jpg'.format(sender.id))
        await event.reply('Profile saved!')

@bot.on(events.NewMessage(pattern='fuck'))
async def badmessage(event):
    await event.delete()

bot.start()
bot.run_until_disconnected()

