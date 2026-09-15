# 📝 Домашнее задание №4
# Тема: Магические методы в классах
# Закрепить работу с магическими методами:
# __add__ __sub__ __mul__ __truediv__
# и научиться работать с логикой внутри класса.


# В начале файла создайте словарь курсов валют относительно сома.
# ключ — валюта
# значение — сколько сомов стоит 1 единица валюты
rates = {
   "KGS": 1,
   "USD": 89,
   "EUR": 96,
   "RUB": 1.2
}


# Создайте класс Money.
# 🔹 Атрибуты класса
# В конструкторе должны быть два атрибута:
# amount — сумма денег, currency — валюта


class Money():
   def __init__(self, amount, currency):
      self.amount = amount
      self.currency = currency
 
 
# 🔹 Метод конвертации
# В классе должен быть метод:
# convert_to_kgs() Этот метод должен переводить любую валюту в сомы.
   def convert_to_kgs(self):
      if self.currency == 'USD':
        return self.amount * rates[self.currency]
      elif self.currency == 'EUR':
        return self.currency * rates[self.currency]
      elif self.currency == 'RUB':
        return self.currency * rates[self.currency]
      elif self.currency == 'SOM':
        return self.currency * rates[self.currency]
        

# Пример:
# 100 USD → 8900 KGS
 

# 🔹 Магические методы
# Реализуйте следующие магические методы:
# __add__
# Сложение денег.
# money1 + money2
 
# Если валюты разные, сначала нужно конвертировать их в сомы, затем выполнить сложение.
# __sub__

# Вычитание денег.
# money1 - money2

# Также нужно учитывать конвертацию валют.
# __mul__

# Умножение денег на число.

# Пример:
# money * 3

# __truediv__
# Деление денег на число.

# Пример:
# money / 2


# 🔹 Метод __str__
# Чтобы объект красиво выводился.

# Пример:
# print(money)

# Вывод:
# 100 USD

 

# 📌 Пример использования

 

# money1 = Money(100, "USD")
# money2 = Money(5000, "KGS")

# result = money1 + money2

# print(result)