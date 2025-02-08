import pandas as pd

# Создаем пустой DataFrame для хранения участников
columns = ['Имя', 'Фамилия', 'Адрес', 'Телефон', 'Электронная почта']
participants_df = pd.DataFrame(columns=columns)

# Функция для добавления участника
def add_participant(name, surname, address, phone, email):
    global participants_df
    new_participant = pd.DataFrame([[name, surname, address, phone, email]], columns=columns)
    participants_df = pd.concat([participants_df, new_participant], ignore_index=True)

# Функция для сохранения таблицы в файл
def save_to_file(filename='participants.xlsx'):
    participants_df.to_excel(filename, index=False)

# Пример добавления участника
add_participant('Иван', 'Иванов', 'Москва, ул. Пушкина, д. 1', '1234567890', 'ivan@example.com')
add_participant('Мария', 'Петрова', 'Санкт-Петербург, ул. Ленина, д. 2', '0987654321', 'maria@example.com')

# Сохраняем данные в файл
save_to_file()
