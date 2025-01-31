# Тайный Санта Бот

Тайный Санта Бот — это Telegram-бот, который помогает организовать игру "Тайный Санта" среди группы друзей, коллег или знакомых. Бот автоматически распределяет участников, отправляет каждому имя его "получателя" и напоминает о необходимости отправить подарок.

**Основные функции бота:**
- создание игры
- регистрация участников в игре
- жеребьевка игроков
- возможность выбора передачи подарков
- выбор цены для подарка

**Установка**  
Для работы вам понадобиться:
- Python 3
- Бот в Telegram ( можно создать через BotFather )

**Настройка бота**
- создаем нового бота через @BotFather в телеграме коммандой "/newbot"
- получаем токен который вводим в файл "cod"
bot = Bot(token='YOUR_TOKEN')
