from telethon import TelegramClient
from creds import *

async def main():

    me = await bot.get_me()
    print(me.stringify())
    print(me.username)

    message = await bot.send_message(
        'Arjunrao1234',
        'This message has **bold**, `code`, __italics__ and '
        'a [nice website](https://example.com)!',
        link_preview=False
    )

    print(message.raw_text)
    #await bot.send_message('Arjunrao1234','testing function')
    await message.reply('Cool!')


with bot:
    bot.loop.run_until_complete(main())
# with bot:
#     bot.loop.run_until_complete(bot.send_message('Arjunrao1234','Hello, This is ArjunBot!'))