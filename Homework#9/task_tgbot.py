import telebot
import random
import json

token = '5999530771:AAGg4MiXzB4kcc6jPq9Iee83yIar3s2leaQ'

bot = telebot.TeleBot(token)

with open('films.json', 'r', encoding='utf-8') as f:
    some_dict = json.load(f)
with open('countries.json', 'r', encoding='utf-8') as c:
    some_dict1 = json.load(c)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Фильмы')
    item2 = telebot.types.KeyboardButton('Столицы стран')
    item3 = telebot.types.KeyboardButton('Квадрат числа')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Добро пожаловать! Выбери нужный пункт меню: ', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'фильмы':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        item1 = telebot.types.KeyboardButton('Побег из Шоушенка')
        item2 = telebot.types.KeyboardButton('Начало')
        item3 = telebot.types.KeyboardButton('Джокер')
        item4 = telebot.types.KeyboardButton('Эрин Брокович')
        item5 = telebot.types.KeyboardButton('1+1')
        item6 = telebot.types.KeyboardButton('Назад в будущее')

        markup.add(item1, item2, item3, item4, item5, item6)

        bot.send_message(message.chat.id, 'Выберите фильм, чтобы узнать его описание', reply_markup=markup)
        bot.register_next_step_handler(message, films)
    elif message.text.lower() == 'столицы стран':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        item1 = telebot.types.KeyboardButton('Россия')
        item2 = telebot.types.KeyboardButton('Австралия')
        item3 = telebot.types.KeyboardButton('Египед')
        item4 = telebot.types.KeyboardButton('США')
        item5 = telebot.types.KeyboardButton('Италия')
        item6 = telebot.types.KeyboardButton('Германия')

        markup.add(item1, item2, item3, item4, item5, item6)

        bot.send_message(message.chat.id, 'Выберите страну, чтобы узнать ее столицу', reply_markup=markup)
        bot.register_next_step_handler(message, countries)
    elif message.text.lower() == 'квадрат числа':
        bot.send_message(message.chat.id, 'Напиши, какое число возвести в квадрат')
        bot.register_next_step_handler(message, square)


@bot.message_handler(content_types=['text'])
def films(message):
    bot.send_message(message.chat.id, some_dict[message.text])

@bot.message_handler(content_types=['text'])
def countries(message):
    bot.send_message(message.chat.id, some_dict1[message.text])

@bot.message_handler(content_types=['text'])
def square(message):
    num = int(message.text)
    bot.send_message(message.chat.id, f'{num*num}')

bot.polling(none_stop=True)