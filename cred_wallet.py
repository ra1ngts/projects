"""Кредитные кошельки."""
from abc import ABC


class Wallet(ABC):
    def __init__(self, name: str, type_: str = "General"):
        self.balance: int = 0
        self.name: str = name
        self.type_: str = type_

    def get_balance(self) -> int:  # typing - подсказка для разработчика.
        return self.balance

    def change_balance(self, value: int):
        if self.balance + value < 0:
            print(f"У вас недостаточный баланс: {self.balance}")
        else:
            self.balance += value


class CreditBalance:

    def change_balance(self, value: int):
        if self.balance + value < self.limit:
            print(f"У вас недостаточный баланс: {self.balance}")
        else:
            self.balance += value


class ProBalance:

    def change_balance(self, value: int):
        if self.balance + value * 0.95 < 0:
            print(f"У вас недостаточный баланс: {self.balance}")
        else:
            self.balance += value * 0.95 if self.balance + value * 0.95 < self.balance else value


class CreditCard(CreditBalance, Wallet):
    def __init__(self, name, limit=-1000):
        self.limit = limit
        super().__init__(name)


class Card(Wallet):
    def __init__(self, name):
        super().__init__(name)

    def change_type(self):
        if self.balance < 100:
            print(f"У вас недостаточный баланс: {self.balance}")
        else:
            self.balance -= 100
            card_ = ProCard(self.name)
            card_.balance = self.balance
            return card_


class ProCard(ProBalance, Wallet):
    def __init__(self, name, type_="PRO"):
        super().__init__(name, type_)


card = ProCard("Sam")
print(card.get_balance())
card.change_balance(1000)
print(card.get_balance())
card.change_balance(-800)
print(card.get_balance())
card.change_balance(-250)
print(card.get_balance())
