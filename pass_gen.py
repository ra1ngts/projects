"""Генератор паролей."""
from random import sample
from string import ascii_letters, ascii_uppercase, digits

letters = ascii_letters + ascii_uppercase + digits + "!?_"
len_pass = 8
uniq_pass = "".join(sample(letters, len_pass))
print()
print("Генератор паролей")
print("-" * 17)
print(f"Уникальный пароль: {uniq_pass}")
print("-" * 17)
