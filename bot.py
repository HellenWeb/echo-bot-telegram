
# Modules

import config
import telebot
from telebot import types

# Default Variebles

bot = telebot.TeleBot(config.token)

# Logic Bot

@bot.message_handler(content_types=['text'])
def send_you_message(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.infinity_polling()

# || \\

