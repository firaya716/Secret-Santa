import telebot
import json
import random
from telebot import types

# Инициализация бота
API_TOKEN = 'TOKEN'  # Замените на свой токен
bot = telebot.TeleBot(API_TOKEN)

# Переменные для хранения состояния
user_states = {}  # Словарь для хранения состояний пользователей

# Функция для загрузки данных из JSON
def load_data():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            if 'users' not in data:
                data['users'] = {}
            if 'games' not in data:
                data['games'] = {}
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {"users": {}, "games": {}}

# Функция для сохранения данных в JSON
def save_data(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    register_button = types.KeyboardButton("Зарегистрироваться")
    markup.add(register_button)
    
    bot.send_message(message.chat.id, "Добро пожаловать в Тайного Санту! Нажмите кнопку ниже для регистрации.", reply_markup=markup)

# Регистрация пользователя
@bot.message_handler(func=lambda message: message.text == "Зарегистрироваться")
def register(message):
    user_id = str(message.from_user.id)
    
    if user_id in user_states:
        bot.send_message(message.chat.id, "Вы уже находитесь в процессе регистрации. Пожалуйста, завершите его.")
        return

    user_states[user_id] = 'waiting_for_name'
    bot.send_message(message.chat.id, "Пожалуйста, введите ваше ИМЯ:")

@bot.message_handler(func=lambda message: str(message.from_user.id) in user_states and user_states[str(message.from_user.id)] == 'waiting_for_name')
def get_name(message):
    user_id = str(message.from_user.id)
    name = message.text.strip()
    
    user_states[user_id] = 'waiting_for_surname'
    user_states[user_id + '_name'] = name
    bot.send_message(message.chat.id, "Спасибо! Теперь введите вашу ФАМИЛИЮ:")

@bot.message_handler(func=lambda message: str(message.from_user.id) in user_states and user_states[str(message.from_user.id)] == 'waiting_for_surname')
def get_surname(message):
    user_id = str(message.from_user.id)
    surname = message.text.strip()
    
    data = load_data()
    username = message.from_user.username or "Без имени"

    # Сохраняем данные пользователя
    data['users'][user_id] = {
        "points": 0,
        "username": username,
        "name": user_states[user_id + '_name'],
        "surname": surname,
        "game": None,
        "santa": None  # Поле для хранения назначенного Тайного Санты
    }
    
    save_data(data)
    del user_states[user_id]  # Удаляем состояние пользователя
    
# Показать основную клавиатуру
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    create_game_button = types.KeyboardButton("Создать игру")
    join_game_button = types.KeyboardButton("Присоединиться к игре")
    markup.add(create_game_button, join_game_button)
    
    bot.send_message(message.chat.id, "Вы успешно зарегистрированы! Выберите действие:", reply_markup=markup)


# Создание игры
@bot.message_handler(func=lambda message: message.text == "Создать игру")
def create_game(message):
    user_id = str(message.from_user.id)
    
    if user_id in user_states:
        bot.send_message(message.chat.id, "Вы уже находитесь в процессе создания игры.")
        return

    user_states[user_id] = 'waiting_for_game_name'
    bot.send_message(message.chat.id, "Введите название игры:")

@bot.message_handler(func=lambda message: str(message.from_user.id) in user_states and user_states[str(message.from_user.id)] == 'waiting_for_game_name')
def get_game_name(message):
    user_id = str(message.from_user.id)
    game_name = message.text.strip()
    
    data = load_data()
    game_id = str(len(data['games']) + 1)  # Генерируем ID игры как строку
    data['games'][game_id] = {"name": game_name, "players": []}  # Сохраняем игру в словаре

    # Обновляем информацию о пользователе
    data['users'][user_id]["game"] = game_id            
    save_data(data)  # Сохраняем изменения в файле

    del user_states[user_id]  # Удаляем состояние после обработки
    
    bot.send_message(message.chat.id, f"Игра '{game_name}' создана с ID: {game_id}.")

# Присоединение к игре
@bot.message_handler(func=lambda message: message.text == "Присоединиться к игре")
def join_game(message):
    user_id = str(message.from_user.id)

    if user_id in user_states:
        bot.send_message(message.chat.id, "Вы уже находитесь в процессе присоединения к игре.")
        return

    user_states[user_id] = 'waiting_for_game_id'
    bot.send_message(message.chat.id, "Пожалуйста, введите ID игры.")

@bot.message_handler(func=lambda message: str(message.from_user.id) in user_states and user_states[str(message.from_user.id)] == 'waiting_for_game_id')
def get_game_id(message):
    user_id = str(message.from_user.id)
    game_id = message.text.strip()
    
    data = load_data()

    if game_id in data['games']:
        game_name = data['games'][game_id]["name"]
        
        # Проверка на существование пользователя
        if user_id not in data['users']:
            data['users'][user_id] = {
                "username": message.from_user.username or "Без имени",
                "game": None
            }
        
        data['games'][game_id]["players"].append(data['users'][user_id]["username"])  # Добавляем игрока в игру
        data['users'][user_id]["game"] = game_id  # Обновляем информацию о пользователе                
        save_data(data)  # Сохраняем изменения в файле
        
        bot.send_message(message.chat.id, f"Вы присоединились к игре '{game_name}'.")
        del user_states[user_id]  # Удаляем состояние после обработки
        show_game_options_keyboard(message.chat.id)  # Показать клавиатуру с опциями игры
    else:
        bot.send_message(message.chat.id, "Неверный ID игры.")
        del user_states[user_id]  # Удаляем состояние после обработки

def show_game_options_keyboard(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    view_players_button = types.KeyboardButton("Просмотр игроков")
    assign_santa_button = types.KeyboardButton("Назначить Тайного Санту")
    markup.add(view_players_button, assign_santa_button)
    bot.send_message(chat_id, "Выберите действие:", reply_markup=markup)

    

@bot.message_handler(func=lambda message: message.text == "Просмотр игроков")
def view_players(message):
    global data  # Указываем, что используем глобальную переменную data
    user_id = str(message.from_user.id)

    # Загружаем данные из файла
    data = load_data()
    
    user_game_id = data['users'].get(user_id, {}).get("game")  # Получаем ID игры пользователя
    if user_game_id is None:
        bot.send_message(message.chat.id, "Вы не присоединились ни к одной игре.")
        return

    players_in_game = []
    
    for user in data['users'].values():
        if user.get("game") == user_game_id:
            name = user.get('name', 'Без имени')
            surname = user.get('surname', 'Без фамилии')
            username = user.get('username', 'Без имени пользователя')
            players_in_game.append(f"{name} {surname} (@{username})")
    
    if players_in_game:
        players_list = "\n".join(players_in_game)
        bot.send_message(message.chat.id, f"Игроки в вашей игре:\n{players_list}")
    else:
        bot.send_message(message.chat.id, "В вашей игре пока нет участников.")
    
    # Показать клавиатуру с опциями игры снова
    show_game_options_keyboard(message.chat.id)
    

@bot.message_handler(func=lambda message: message.text == "Назначить Тайного Санту")
def assign_santa(message):
    data = load_data()
    
    players = []  # Список игроков, которые присоединились к игре
    for user_id, user_info in data['users'].items():
        if user_info.get("game") is not None:  # Проверяем, что игрок присоединился к игре
            players.append(user_id)

    if len(players) < 2:
        bot.send_message(message.chat.id, "Недостаточно игроков для назначения Тайного Санты.")
        return

    # Логика назначения Тайного Санты
    random.shuffle(players)  # Перемешиваем список игроков
    
    for i in range(len(players)):
        santa = players[i]
        recipient = players[(i + 1) % len(players)]  # Следующий пользователь получает предыдущего как Тайного Санту
        data['users'][santa]['santa'] = recipient  # Сохраняем назначенного Тайному Санте
    
    save_data(data)

    # Убираем кнопку "Назначить Тайного Санту" и показываем кнопку "Кто мой Тайный Санта?"
    show_santa_button(message.chat.id)

# Показать кнопку "Показать Тайного Санту"
def show_santa_button(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    who_is_my_santa_button = types.KeyboardButton("Показать Тайного Санту")
    markup.add(who_is_my_santa_button)
    
    bot.send_message(chat_id, "Нажмите на кнопку ниже, чтобы узнать для кого вы Тайный Санта:", reply_markup=markup)
    

# Узнать, кто мой Тайный Санта
@bot.message_handler(func=lambda message: message.text == "Показать Тайного Санту")
def who_is_my_santa(message):
    user_id = str(message.from_user.id)
    
    data = load_data()  # Загружаем данные для проверки
    users = data['users']

    # Получаем список участников игры
    players_in_game = list(users.keys())

    # Перемешиваем список участников и назначаем Тайного Санта
    random.shuffle(players_in_game)
    assignments = {players_in_game[i]: players_in_game[(i + 1) % len(players_in_game)] for i in range(len(players_in_game))}
            
    # Сохраняем назначения в данных пользователей
    for player in players_in_game:
        users[player]["santa"] = assignments[player]
                
    save_data({"users": users, "games": data["games"]})  # Сохраняем изменения в файле

    # Отправляем каждому участнику его Тайного Санта
    for player in players_in_game:
        santa_username = users[assignments[player]]["username"]
        bot.send_message(player, f"Вы Тайный Санта для: {santa_username}")


    # Убираем клавиатуру после нажатия кнопки
    bot.send_message(message.chat.id, "Спасибо! Теперь вы знаете, кто ваш Тайный Санта.", reply_markup=types.ReplyKeyboardRemove())

    bot.send_message(message.chat.id, "🎅 Дорогие участники! Поздравляем вас с успешным назначением Тайного Санты! 🎁Пусть это время будет наполнено радостью, сюрпризами и хорошим настроением. Желаем вам увлекательной и веселой игры!")     
    bot.send_message(message.chat.id, "Для того чтобы начать новую игру, пожалуйства, нажмите на /start")

# Запуск бота
bot.polling(none_stop=True)
