CREATE TABLE phonebook
(id SERIAL PRIMARY KEY,
name TEXT NOT NULL,
phone TEXT NOT NULL);

COPY phonebook(name, phone)
FROM 'C:\Users\zhuma\PycharmProjects\TSIS10\phonebook'
DELIMITER ','
CSV HEADER;