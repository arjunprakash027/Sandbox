import telebot
import yfinance as yf
BOT_TOKEN = ""

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start','hello'])
def welcome(message):
    print("bot invoked")
    bot.reply_to(message,"Hi frds i am the naresh")

@bot.message_handler(commands=['current'])
def count(message):
    text = "enter the name of the indian stock"
    sent_message = bot.send_message(message.chat.id,text,parse_mode='Markdown')
    bot.register_next_step_handler(sent_message,get_price)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    print(message)
    print(message.chat.id)
    vedio = open("rr.mp4","rb")
    bot.send_video(message.chat.id,vedio)
    #bot.send_message(message.chat.id,f'{message.text} is not a valid command',parse_mode='Markdown')


def get_price(message):
    stock = message.text
    ticker = "{}.NS".format(stock.upper())
    try:
        stock_price = yf.Ticker(ticker)
        price = stock_price.info["currentPrice"]
        #print(stock_price.info)
        bot.send_message(message.chat.id,"The current price of {} is {}".format(stock.upper(),price))
    except:
        bot.send_message(message.chat.id,"Please enter a valid stock name")
    

bot.infinity_polling()