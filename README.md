# Тайный Санта Бот @SecretSanta4_bot

Этот проект представляет собой телеграм-бота для игры "Тайный Санта". Пользователи могут регистрироваться, создавать и присоединяться к играм, назначать Тайных Санта и угадывать их.

## Функции

- регистрация пользователей: Пользователи могут зарегистрироваться, указав свое имя и фамилию
- создание игры: Пользователи могут создавать новые игры, задавая название
- присоединение к игре: Пользователи могут присоединяться к уже существующим играм
- назначение Тайных Сант: Бот случайным образом назначает Тайных Сант участникам игры.
  
## Что необходимо для работы бота 
- установить Python https://www.python.org/downloads/
- установить на компьютер необходимую библиотеку telebot (pyTelegramBotAPI). Для этого открываем командную строку и прописываем  `pip install pyTelegramBotAPI`.
- аккаунт в телеграмме

## Настройка бота
- создаем нового бота через @BotFather в телеграме коммандой "/newbot"
- получаем токен который копируем
- открываем фаил "cod.py" через удобную вам среду
- в строке "API_TOKEN" пишем ранее скопированный ваш токен бота
  ```
  API_TOKEN = 'TOKEN'
  ```
- запускаем бота
  
## Использование

- Откройте Telegram и найдите вашего бота

### Начало работы

- Для активации бота нужно отправить команду /start

### Регистрация пользователя

- Для регистрации необходимо нажать кнопку "Зарегистрироваться"
- Бот запросит ввод имени и фамилии
- После успешной регистрации будет получено подтверждение

### Создание игры

- Для создания новой игры следует нажать кнопку "Создать игру"
- Бот запросит название игры

### Присоединение к игре

- Для присоединения к существующей игре нужно отправить команду "Присоединиться к игре"
- Бот попросит ввести ID игры
- После успешного присоединения будет получено уведомление

### Назначение Тайных Сант

- После завершения регистрации следует нажать на кнопку "Назначить Тайного Санту" для распределения участников.

### Получение информации о Тайном Санте

- Для получения информации о Тайном Санте нужно нажать на кнопку "Показать Тайного Санту"
- Бот ответит с именем Тайного Санты


