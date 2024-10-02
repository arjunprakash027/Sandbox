from telethon import TelegramClient,events, Button
from creds import *

import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

@bot.on(events.NewMessage)
async def reply(event):
    logging.info(event.raw_text)
    user = await event.get_sender()
    sender = user.username
    logging.info("{} accessed the bot".format(sender))
    await event.respond(
        "Welcome to the test group guys!",
        buttons=Button.inline("🚖 Start Booking", data="start_order"),
    )

@bot.on(events.CallbackQuery(data="start_order"))
async def callback(event):
    await event.edit("Choose your destination",
        buttons=[
            [Button.inline("🏠 Home", data="home")],
            [Button.inline("🏢 Office", data="office")],
            [Button.inline("🏫 School", data="school")],
        ]
    )
    logging.info("Callback query from {}".format(event.sender.username))

@bot.on(events.CallbackQuery(data="home"))
async def callback(event):
    logging.info(event.data.decode("utf-8"))
bot.start()
bot.run_until_disconnected()

