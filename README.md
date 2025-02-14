# Тайный Санта Бот @SecretSanta4_bot

Этот проект представляет собой Телеграм-бота для игры "Тайный Санта". Пользователи могут регистрироваться, создавать и присоединяться к играм, назначать Тайных Санта и угадывать их.

## Функции

- Регистрация пользователей
- Создание и присоединение к играм
- Назначение Тайных Санта
- Угадывание Тайного Санты с системой баллов
- Просмотр текущих баллов


## Что необходимо для работы бота 
- установить Python https://www.python.org/downloads/
- установить на компьютер необходимую библиотеку telebot (pyTelegramBotAPI). Для этого открываем командную строку и прописываем  `pip install pyTelegramBotAPI`.
- аккаунт в телеграмме
- cоздать файл data.json для хранения данных о пользователях и играх. Вы можете оставить его пустым, он будет заполнен автоматически при первом запуске.


## Настройка бота
- создаем нового бота через @BotFather в телеграме коммандой "/newbot"
- получаем токен который копируем
- открываем фаил "cod.py" через удобную вам среду
- в строке "bot" пишем ранее скопированный ваш токен бота
  ```rb
  bot = telebot.TeleBot('YOUR_TOKEN')
  ```
- запускаем бота
  
## Использование

1. Откройте Telegram и найдите вашего бота.
2. Используйте команду /start для начала работы.
3. Зарегистрируйтесь с помощью команды /register.
4. Выберите одно из доступных действий, используя кнопки меню.
