import moduls

# Вызов функции get_records_by_pattern
pattern = "Jane"
rows = moduls.get_records_by_pattern(pattern)
print(rows)

# Вызов функции insert_or_update_user
name = "John Doe"
phone = "123-456-7890"
moduls.insert_or_update_user(name, phone)

# Вызов функции insert_many_users
users = [("Jane Smith", "555-123-4567"), ("Bob Johnson", "555-555-5555"), ("Alice Cooper", "123-45-6789")]
moduls.insert_many_users(users)

# Вызов функции get_records_with_pagination
limit = 2
offset = 1
result = moduls.get_records_with_pagination(limit, offset)
print(result)

# Вызов функции delete_user_by_name
name = "Bob Johnson"
moduls.delete_user_by_name(name)

# Вызов функции delete_user_by_phone
phone = "123-45-6789"
moduls.delete_user_by_phone(phone)