import psycopg2

def get_records_by_pattern(pattern):
    conn = psycopg2.connect(database="phonebook", user="postgres", password="admin", host="localhost", port="5432")
    cur = conn.cursor()
    cur.callproc('get_records_by_pattern', [pattern])
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def insert_or_update_user(name, phone):
    conn = psycopg2.connect(database="phonebook", user="postgres", password="admin", host="localhost", port="5432")
    cur = conn.cursor()
    cur.callproc('insert_or_update_user', [name, phone])
    conn.commit()
    cur.close()
    conn.close()

def insert_many_users(users):
    conn = psycopg2.connect(database="phonebook", user="postgres", password="admin", host="localhost", port="5432")
    cur = conn.cursor()
    for user in users:
        name = user[0]
        phone = user[1]
        if validate_phone(phone):
            cur.callproc('insert_or_update_user', [name, phone])
        else:
            print(f"Incorrect phone format for user {name}: {phone}")
    conn.commit()
    cur.close()
    conn.close()

def get_records_with_pagination(limit, offset):
    conn = psycopg2.connect(database="phonebook", user="postgres", password="admin", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM phonebook")
    total_count = cur.fetchone()[0]
    cur.execute("SELECT name, phone FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return {"data": rows, "total_count": total_count}

def delete_user_by_name(name):
    conn = psycopg2.connect(database="phonebook", user="postgres", password="admin", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name = %s", [name])
    conn.commit()
    cur.close()
    conn.close()

def delete_user_by_phone(phone):
    conn = psycopg2.connect(database="phonebook", user="postgres", password="admin", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE phone = %s", [phone])
    conn.commit()
    cur.close()
    conn.close()