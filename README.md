**# Тайный Санта Бот

Тайный Санта Бот — это Telegram-бот, который помогает организовать игру "Тайный Санта" среди группы друзей, коллег или знакомых. Бот автоматически распределяет участников, отправляет каждому имя его "получателя" и напоминает о необходимости отправить подарок.

**Основные функции бота:**
- выбор отправки подарка
- выбор стоймости подарка

**Установка**  
Для работы вам понадобиться:
- установить Python https://www.python.org/downloads/
- установить на компьютер необходимую библиотеку telebot (pyTelegramBotAPI). Для этого открываем командную строку и прописываем pip install pyTelegramBotAPI.
- аккаунт в телеграмме

**Настройка бота**
- создаем нового бота через @BotFather в телеграме коммандой "/newbot"
- получаем токен который копируем
- открываем фаил "cod.py" через удобную вам среду
- в строке "bot" пишем ранее скопированный ваш токен бота
```
# bot = telebot.TeleBot('YOUR_TOKEN')
```
- запускаем бота

**Будет добавлено**
- создание игры
- приглашать игроков
- смотреть кто играет
- жеребьевка игроков
