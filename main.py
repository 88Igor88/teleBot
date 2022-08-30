import telebot
from os import remove
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

Bot = telebot.TeleBot("5561159253:AAH6bKKGMiZa6Cp6HrcBQtE4Gd7gAlvq-7A")


@Bot.message_handler(commands=['start'])
def start(message):
    but_1 = KeyboardButton(text="Привет")
    but_2 = KeyboardButton(text="Пока")
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(but_1, but_2).add(but_1, but_2)
    Bot.send_message(message.chat.id, "Привет, привет! Я надоедливый бот Повторюшка. "
                                      "Буду повторять все, что ты мне напишешь, Ахахахахаах", reply_markup=[keyboard])


@Bot.message_handler(commands=['help'])
def help(message):
    Bot.send_message(message.chat.id, "Привет я бот для простых разговоров.")


@Bot.message_handler(commands=['button'])
def button_(message):
    bu1 = KeyboardButton(text="1")
    bu2 = KeyboardButton(text="2")
    bu3 = KeyboardButton(text="3")
    bu4 = KeyboardButton(text="4")
    bu5 = KeyboardButton(text="5")
    bu6 = KeyboardButton(text="6")
    keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(bu1, bu2, bu3).add(bu4, bu5, bu6)
    Bot.send_message(message.chat.id, "Выбери кнопку", reply_markup=[keyboard1])


@Bot.message_handler(content_types=["text"])
def repeat(message):
    if message.text == "Привет":
        button_(message)
    if message.text == "Пока":
        Bot.send_message(message.chat.id, "какой ты не культурный!")

    if message.text == "1":
        Bot.send_message(message.chat.id, "Привет! ты нажал кнопку 1")
    if message.text == "2":
        bu_1 = KeyboardButton(text="да")
        bu_2 = KeyboardButton(text="нет")
        bu_n = KeyboardButton(text="не знаю")
        keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(bu_1, bu_2, )
        Bot.send_message(message.chat.id, "Понравилось тебе разговаривать?", reply_markup=[keyboard2])
        if message.text == "да":
            Bot.send_message(message.chat.id, "Спасибо")
    if message.text == "3":
        Bot.send_message(message.chat.id, "пока!")
    if message.text == "4":
        Bot.send_message(message.chat.id, "какой твой любимый цвет?")
        if message.text == "красный" or message.text == "Красный":
            Bot.send_message(message.chat.id, "Мой такой же!")

        else:
            Bot.send_message(message.chat.id, "понятно")
    if message.text == "5":
        Bot.send_message(message.chat.id, "какое твоё любимое время года?")
        if message.text == "Все времена года" or message.text == "все времена года":
            Bot.send_message(message.chat.id, "Я бы также ответил!")
        else:
            Bot.send_message(message.chat.id, "хорошо")
    if message.text == "6":
        Bot.send_message(message.chat.id, "Как тебя зовут?")
        if message.text == "Игорь" or "Ксения":
            Bot.send_message(message.chat.id, "Понятно")
        else:
            Bot.send_message(message.chat.id, "Понятно")


@Bot.message_handler(content_types=['photo'])
def Photo(message):
    file_id = message.photo[-1].file_id
    file_i = Bot.get_file(file_id)
    file_download = Bot.download_file(file_i.file_path)
    with open("image", 'wb') as new_file:
        new_file.write(file_download)
    file_open = open("image", 'rb')
    Bot.send_photo(message.chat.id, file_open)
    file_open.close()
    remove("image")
Bot.infinity_polling()
