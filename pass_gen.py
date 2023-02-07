"""Генератор паролей."""
import random
import string

letters = string.ascii_letters + string.ascii_uppercase + string.digits + "!?_"
len_pass = 8
uniq_pass = "".join(random.sample(letters, len_pass))
print()
print("Генератор паролей")
print("-" * 17)
print(f"Уникальный пароль: {uniq_pass}")
print("-" * 17)
