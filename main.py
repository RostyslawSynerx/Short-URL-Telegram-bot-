import telebot
import pyshorteners

token = 'TOKEN'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Отправьте ссылку и бот сделает её короче.\nSend a link and the bot will make it shorter.')

@bot.message_handler(func=lambda message: True)
def url(message):
    pys = pyshorteners.Shortener()
    short_url = pys.tinyurl.short(message.text)
    bot.send_message(message.chat.id, short_url)

bot.infinity_polling()







