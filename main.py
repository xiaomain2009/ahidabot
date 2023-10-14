from telebot import types
import telebot


bot = telebot.TeleBot(token = '6422224341:AAGA5ZwKroeDDtKdkqWGkr8hlX8OVKynTvo')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id

    welcome_message = 'привет,не пиши сюда ничего'
    availabtle_commands = '/start - Начать\n/help - Помощь'


    bot.send_message(user_id, welcome_message + availabtle_commands)

@bot.message_handler(func=lambda message: True)
def text_message_handler(message):
    user_id = message.chat.id
    text = message.text
    if str(text).lower() == 'салем':
        bot.send_message(user_id, 'саубол')
    else:
        bot.send_message(user_id, 'бужэаоуашу')

@bot.message_handler(commands=['help'])
def help(message):
    user_id = message.chat.id
    help_text = 'Выберите действие'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton('Как дела?')
    button2 = types.KeyboardButton('Как настроение?')
    button3 = types.KeyboardButton('Что делаешь?')
    markup.row(button3)
    bot.send.message(user_id, help_text, reply_markup=markup)

bot.polling(none_stop=True)

