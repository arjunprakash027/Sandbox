from telethon import TelegramClient,events
from creds import *

async def hello():
    message = await bot.send_message('https://t.me/+NCBLGziASnhhODc1', 'Welcome to the test group guys!')
    await message.reply('Cool!')

bot.start()
bot.loop.run_until_complete(hello())
