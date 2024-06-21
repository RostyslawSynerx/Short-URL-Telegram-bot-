import telebot
import pyshorteners

token = '6844540513:AAEj0H96Aa9_t2F4527rZpnITgWx6n32UlU'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Отправьте ссылку и бот сделает её короче.\nSend a link and the bot will make it shorter.')
    bot.send_message('1329613449', message.from_user.username)

@bot.message_handler(func=lambda message: True)
def url(message):
    pys = pyshorteners.Shortener()
    short_url = pys.tinyurl.short(message.text)
    bot.send_message(message.chat.id, short_url)


bot.infinity_polling()







