import telebot #импорт библиотеки telebot
from os import remove
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton
Bot = telebot.TeleBot("5561159253:AAH6bKKGMiZa6Cp6HrcBQtE4Gd7gAlvq-7A") #потключение бота
xm = 10
gm = 100
xdp = 1
gdp = 10
import random #импорт библиотеки random
def keybord_5(): #создание функци
    butor1 = KeyboardButton("Атаковать") #кнопка 1
    butor2 = KeyboardButton("Вернуться в главное меню")#кнопка 2
    butor3 = KeyboardButton("Бежать")#кнопка 3
    keybord_5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(butor1, butor2, butor3) #создание обекта клавиатуры
    return keybord_5 # сохранение переменой keybord_5 с помощю return
hp = 0
yp = 0
hp_kone = 0
dp_kone = 0
xp = 0
dp = 0
monstor_m = 0

@Bot.message_handler(commands=['start']) #декоратор
def start(message):#создание функци
    br_1 = KeyboardButton("Начать игру")#кнопка 1
    info = KeyboardButton("Об игре")#кнопка 2
    keybord = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(br_1,info)#создание обекта клавиатуры
    Bot.send_message(message.chat.id,"хочешь начать играть", reply_markup=[keybord]) #
    global monstor_m
    monstor_m = monstor()
@Bot.message_handler(content_types=["text"]) #декоратор
def text(message):#создание функци
    randomYdar = 0
    global hp,dp,xp,yp,hp_kone,dp_kone,monstor_m
    wi1 = KeyboardButton("Начать сражение")#кнопка 1
    wi2 = KeyboardButton("Вернуться в главное меню")#кнопка 2
    keybord_4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(wi1,wi2)#создание обекта клавиатуры
    if message.text == "Начать игру":#блок if
        perso_1 = KeyboardButton("Эльф")#кнопка 1
        perso_2 = KeyboardButton("Гном")#кнопка 2
        keybord_1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(perso_1,perso_2)#создание обекта клавиатуры
        Bot.send_message(message.chat.id,"Выбери персонажа:",reply_markup=[keybord_1])
    if message.text == "Об игре":#блок if
        Bot.send_message(message.chat.id,"В этой игре вам претстоит сразится с босом и выбрать персонажа с разными професиями! Для начала игры напишите- Начать игру")
    if message.text == "Эльф":#блок if
        hp = 10
        dp = 20
        pe_1 = KeyboardButton("Лучник")
        pe_2 = KeyboardButton("Воин")
        pe_3 = KeyboardButton("Воин на коне")
        pe_4 = KeyboardButton("Маг")
        keybord_2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(pe_1, pe_2, pe_3, pe_4)#создание обекта клавиатуры
        Bot.send_message(message.chat.id,"Ты храбрый эльф и у тебя {} жизней и у тебя {} урона и терерь осталось выбрать професию".format(dp, hp), reply_markup=[keybord_2])
    if message.text == "Лучник":#блок if
        dp += 5
        Bot.send_message(message.chat.id,"Теперь ты меткий лучник у тебя {} жизней и {} урона. Готов к приключению?".format(hp,dp), reply_markup=[keybord_4])
    if message.text == "Воин":#блок if
        dp += 12
        hp += 17
        Bot.send_message(message.chat.id,"Теперь ты сильный воин у тебя {} жизней и {} урона. Готов к приключению?".format(hp, dp),reply_markup=[keybord_4])
    if message.text == "Воин на коне":#блок if
        dp += 7
        hp_kone += 30
        dp_kone += 13
        Bot.send_message(message.chat.id,"Теперь ты сильный воин на коне у тебя {} жизней и {} урона а у коня {} урона а жизней {}. Готов к приключению?".format(hp, dp, dp_kone, hp_kone),reply_markup=[keybord_4])
    if message.text == "Маг":#блок if
        dp += 20
        hp += 10
        Bot.send_message(message.chat.id,"Теперь ты маг у тебя {} жизней и {} урона. Готов к приключению?".format(hp,dp), reply_markup=[keybord_4])
    if message.text == "Гном":#блок if
        hp = 20
        dp = 10
        peg_1 = KeyboardButton("Лучник")
        peg_2 = KeyboardButton("Воин")
        peg_3 = KeyboardButton("Воин на коне")
        peg_4 = KeyboardButton("Маг")
        keybord_3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(peg_1, peg_2, peg_3, peg_4)#создание обекта клавиатуры
        Bot.send_message(message.chat.id,"Ты храбрый гном и у тебя {} жизней и у тебя {} урона и терерь осталось выбрать професию".format(dp, hp), reply_markup=[keybord_3])
    if message.text == "Вернуться в главное меню":#блок if
        hp = 0
        dp = 0
        start(message)
    if message.text == "Начать сражение":#блок if

        random1 = random.randint(1,3)
        if random1 == 1:#блок if
            Bot.send_message(message.chat.id,"Мы пока некого не встретили, пойдем дальше?", reply_markup=[keybord_4])
        if random1 == 2:#блок if
            Bot.send_message(message.chat.id, "А вот и маленький монстр! Монстра зовут {},у него {} жизней и сила удара {}".format(monstor_m[0],monstor_m[1],monstor_m[2]), reply_markup=[keybord_5()])
            Bot.send_animation(message.chat.id, r"https://i.gifer.com/1LsK.gif")
        if random1 == 3:#блок if
            Bot.send_message(message.chat.id, "А вот и сам бос!",reply_markup=[keybord_5()])
    if message.text == "Атаковать":#блок if
        monstor_m[1] -= dp
        xp += 1
        Bot.send_message(message.chat.id,"ты ударил монстра и у него {} жизней и твой опыт: {} и твой уровень: {} он тебя сейчас наверное ударит!".format(monstor_m[1],xp,yp))
        randomYdar = random.randint(1,3)

    if randomYdar == 1:#блок if
        hp -= monstor_m[2]
        Bot.send_message(message.chat.id, "Он тебя ударил и у тебя {} жизней".format(hp))
    elif randomYdar == 2 or randomYdar == 3:#блок if
        Bot.send_message(message.chat.id, "Он тебя не ударил!", reply_markup=[keybord_5()])
    if monstor_m[1] < 0:#блок if
        dp += 5
        hp += 5
        xp += 5
        yp += 1
        if dp_kone > 0:#блок if
            dp_kone += 3
            hp_kone += 3
        monstor_m = monstor()
        Bot.send_message(message.chat.id,"Ты победил монстра и твой урон превысился на 5 но и монстры будут сильней!", reply_markup=[keybord_4])
    if yp == 5:#блок if
        r_1 = KeyboardButton("надеть броню")
        r_2 = KeyboardButton("не надевать броню")
        keybord_6 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(r_1, r_2)#создание обекта клавиатуры
        Bot.send_message(message.chat.id, "ты дошел до 5 уровня и выбери что-нибудь", reply_markup=[keybord_6])
    if hp < 0:#блок if
        xp = 0
        dp = 0
        hp = 0
        if dp_kone > 0:#блок if
            dp_kone = 0
            hp_kone = 0
        Bot.send_message(message.chat.id,"ты проиграл!")
        start(message)
    if message.text == "надеть броню":#блок if
        hp += 10
        Bot.send_message(message.chat.id,"У тебя теперь {} жизней".format(hp),reply_markup=[keybord_4])
    if message.text == "не надевать броню":#блок if
        Bot.send_message(message.chat.id,"у тебя не чего изменилось",reply_markup=keybord_4)
def monstor():#создание функци
    global xm,gm,xdp,gdp
    xm += 5
    gm += 5
    xdp += 5
    gdp += 5
    name_m = ["монстр 1","монстр 2"]
    random_name = random.choice(name_m)
    hp_m = random.randint(xm,gm)
    dp_m = random.randint(xdp, gdp)
    return [random_name, hp_m, dp_m]
Bot.infinity_polling()