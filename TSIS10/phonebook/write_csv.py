import csv

# Открытие файла для записи в кодировке UTF-8
with open('phonebook.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Запись заголовка CSV-файла
    header = ['name', 'phone']
    writer.writerow(header)

    # Запись данных в CSV-файл
    data = [
        ['Pasha Tayler', '123-456-7890'],
        ['Alex Smith', '555-123-4567'],
        ['Mark Kirkh', '555-555-5555']
    ]
    writer.writerows(data)