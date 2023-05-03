def delete_table():
    conn = None
    try:
        # Подключение к базе данных
        conn = psycopg2.connect(**db_config)

        # Создание курсора
        cur = conn.cursor()

        # SQL-запрос для удаления таблицы
        drop_table_query = "DROP TABLE IF EXISTS phonebook;"

        # Выполнение SQL-запроса
        cur.execute(drop_table_query)

        # Подтверждение транзакции
        conn.commit()
        print("Таблица успешно удалена")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при удалении таблицы", error)

    finally:
        # Закрытие курсора и соединения
        if conn:
            cur.close()
            conn.close()
            print("Соединение с PostgreSQL закрыто")
