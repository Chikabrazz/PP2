import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(database="phonebook", user="postgres", password="admin", host="localhost", port="5432")

# Создание таблицы
cur = conn.cursor()
# cur.execute('''CREATE TABLE telbook
#                (id SERIAL PRIMARY KEY,
#                 name TEXT NOT NULL,
#                 phone TEXT NOT NULL);''')
conn.commit()

# Создание записи
def create_record(name, phone):
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()

# Чтение всех записей
def read_all_records():
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Обновление записи по имени
def update_record(name, new_phone):
    cur = conn.cursor()
    cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (new_phone, name))
    conn.commit()

# Удаление записи по имени или номеру телефона
def delete_record(value):
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name=%s OR phone=%s", (value, value))
    conn.commit()

# Закрытие соединения с базой данных
conn.close()