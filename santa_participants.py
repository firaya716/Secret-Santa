import telebot
from telebot import types

bot = telebot.TeleBot('7557750266:AAElnGhdbdevI_LGh_xc-bp6DUa6dAPsKmA')

#start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Этот бот поможет вам организовать игру «Тайный Санта».", reply_markup = menu)

#Создать игру/Мои игры
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
create_game = types.KeyboardButton("Создать игру") #Запоминать созданную "игра"
games = types.KeyboardButton("Мои игры") #Показывать созданные игры
menu.add(create_game,games)

#Кнопка назад
back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_button = types.KeyboardButton("Назад")
back.add(back_button)

#Создать игру
present_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
mail_button = types.KeyboardButton("Почта или доставка") #Записывать адрес в "пользователи"
game_button = types.KeyboardButton("Лично")
back_button = types.KeyboardButton("Назад")
present_menu.add(mail_button,game_button,back_button)

budget_menu = types.ReplyKeyboardMarkup(resize_keyboard =True) #Записать сумму в "игра"
budget100_button = types.KeyboardButton("100")
budget500_button = types.KeyboardButton("500")
budget1000_button = types.KeyboardButton("1000")
budget1500_button = types.KeyboardButton("1500")
budget2000_button = types.KeyboardButton("2000")
back_button = types.KeyboardButton("Назад")
budget_menu.add(budget100_button,budget500_button,budget1000_button,budget1500_button,budget2000_button,back_button)

#Мои игры
games_menu = types.ReplyKeyboardMarkup(resize_keyboard =True)
game1_button = types.KeyboardButton("Игра")#Добавить возможность писать любое название
back_button = types.KeyboardButton("Назад")
games_menu.add(game1_button,back_button)

name_game_menu = types.ReplyKeyboardMarkup(resize_keyboard =True) #должно появляться при написанни любого *названия* игры
invite_button = types.KeyboardButton("Пригласить игрока") #Добавить возможность приглашать игрока
look_button = types.KeyboardButton("Кто играет") #Добавить возможность смотреть кто играет
zherebovka_button = types.KeyboardButton("Жеребьевка") #Добавить возможность жеребьевки
register = types.KeyboardButton("Зарегистрироваться") #Добавить возможность зарегистрироваться
back_button = types.KeyboardButton("Назад")
name_game_menu.add(invite_button,look_button,zherebovka_button,register,back_button)

#text
@bot.message_handler(content_types = ['text'])
def text_message(message):
    if message.text == "Назад":
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup = menu) #Переносить только на 1 меню назад

    elif message.text == "Создать игру": #Создать игру
        bot.send_message(message.chat.id, "Введите название игры", reply_markup = back)
    elif message.text == "Название": #Сделать что бы можно было писать любое название
        bot.send_message(message.chat.id,"Как участники будут дарить подарки?", reply_markup = present_menu)
    elif message.text == "Почта или доставка":
        bot.send_message(message.chat.id,"Вы выбрали «Почтой или доставкой». Т.е. вы все находитесь в разных местах и будете отправлять подарки на домашний адрес. У всех игроков мы попросим ввести свой адрес.", reply_markup = budget_menu)
    elif message.text == "Лично":
        bot.send_message(message.chat.id,"Вы выбрали «Лично». Т.е. вы собирётесь в специально условленном месте и будете лично вручать подарки.", reply_markup = budget_menu)
    elif message.text == "Вы выбрали «Лично». Т.е. вы собирётесь в специально условленном месте и будете лично вручать подарки.":
        bot.send_message(message.chat.id,"Установите бюджет на подарки", reply_markup = budget_menu)
    elif message.text == "Вы выбрали «Почтой или доставкой». Т.е. вы все находитесь в разных местах и будете отправлять подарки на домашний адрес. У всех игроков мы попросим ввести свой адрес.":
        bot.send_message(message.chat.id,"Установите бюджет на подарки", reply_markup = budget_menu)
    elif message.text == "100":
        bot.send_message(message.chat.id,"Игра создана", reply_markup = menu)
    elif message.text == "500":
        bot.send_message(message.chat.id,"Игра создана", reply_markup = menu)
    elif message.text == "1000":
        bot.send_message(message.chat.id,"Игра создана", reply_markup = menu)
    elif message.text == "1500":
        bot.send_message(message.chat.id,"Игра создана", reply_markup = menu)
    elif message.text == "2000":
        bot.send_message(message.chat.id,"Игра создана", reply_markup = menu)
        
    elif message.text == "Мои игры": #Мои игры
        bot.send_message(message.chat.id, "Выберите игру", reply_markup = games_menu)
    elif message.text == "Игра": #Сделать что бы можно было писать любое название
        bot.send_message(message.chat.id,"Хотите пригласить или посмотреть кто играет?", reply_markup = name_game_menu)
    elif message.text == "Жеребьевка":
        bot.send_message(message.chat.id,"Вам выпал: ", reply_markup = name_game_menu) #добавить жеребьевку между игроками 
bot.infinity_polling()
