from telethon import TelegramClient,events, Button
from creds import *
import stripe

import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
stripe.api_key = ''
webhook_secret = ''


@bot.on(events.NewMessage)
async def handle_message(event):
    if event.text == '/pay':
        
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'inr',
                        'unit_amount': 123000,
                        'product_data': {
                            'name': 'membership',
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )
    await event.reply(checkout_session.url)


bot.start()
bot.run_until_disconnected()

