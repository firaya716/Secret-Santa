# Тайный Санта Бот @SecretSanta4_bot

Тайный Санта Бот — это Telegram-бот, который помогает организовать игру "Тайный Санта" среди группы друзей, коллег или знакомых. Бот автоматически распределяет участников, отправляет каждому имя его "получателя" и напоминает о необходимости отправить подарок.

**Основные функции бота**
- создание новой игры
- просмотр всех созданных игр
- выбор способа доставки подарков (посредством почты или лично)
- установка бюджета на подарки

**Что необходимо для работы бота**  
- установить Python https://www.python.org/downloads/
- установить на компьютер необходимую библиотеку telebot (pyTelegramBotAPI). Для этого открываем командную строку и прописываем  `pip install pyTelegramBotAPI`.
- аккаунт в телеграмме

**Настройка бота**
- создаем нового бота через @BotFather в телеграме коммандой "/newbot"
- получаем токен который копируем
- открываем фаил "cod.py" через удобную вам среду
- в строке "bot" пишем ранее скопированный ваш токен бота
  ```rb
  bot = telebot.TeleBot('YOUR_TOKEN')
  ```
- запускаем бота
  
## Начало работы
После запуска бота, отправьте команду `/start`, чтобы начать взаимодействие с ботом. Бот ответит приветственным сообщением и предложит вам варианты действий  
  
**Основное меню**  
Главное меню предоставляет два варианта:
- *Создать игру* - для начала нового игрового процесса.
- *Мои игры* - для просмотра уже созданных игр.  

**Меню "Создание игры"**  
1. Выберите *Создать игру*.
2. Введите название игры.
3. Выберите, как будут дариться подарки:
   - Почта или доставка.
   - Лично.
4. Установите бюджет на подарки из предложенных вариантов: 100, 500, 1000, 1500, 2000.
  
**Способы доставки подарков**  
- **Почта или доставка**: В этом случае игроки вводят свои адреса для доставки подарков.
- **Лично**: Игроки собираются в одном месте для обмена подарками.  
  
**Меню "Мои игры"**  
В этом меню можно просмотреть все созданные игры, а также управлять ими. На данный момент доступна возможность приглашать других игроков и проверять, кто участвует в игре.  
  
**Будет добавлено**
- создание игры
- приглашать игроков
- смотреть кто играет
- жеребьевка игроков
