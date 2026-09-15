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
# Пример: 100 USD → 8900 KGS
  def convert_to_kgs(self):
    if self.currency == 'USD':
      return self.amount * rates[self.currency]
    elif self.currency == 'EUR':
      return self.amount * rates[self.currency]
    elif self.currency == 'RUB':
      return self.amount * rates[self.currency]
    elif self.currency == 'KGS':
      return self.amount * rates[self.currency]
    else:
      return 'неверная валюта'


# 🔹 Магические методы
# Реализуйте следующие магические методы:
# __add__Сложение денег: money1 + money2
# Если валюты разные, сначала нужно конвертировать их в сомы, затем выполнить сложение.

  def __add__(self, other):   
    total = int(self.convert_to_kgs()) + int(other.convert_to_kgs())
    return Money(total,'kgs')
    
  
# __sub__Вычитание денег:money1 - money2
# Также нужно учитывать конвертацию валют.
  def __sub__(self, other):
    diff = int(self.convert_to_kgs())-int(other.convert_to_kgs())
    return Money(diff,'kgs')


# __mul__Умножение денег на число: money * 3
  def __mul__(self, number):
    return Money(self.amount * number,self.currency)


# __truediv__ Деление денег на число: money / 2
  def __truediv__(self, number):
    return Money(int(self.amount / number), self.currency)

# 🔹 Метод __str__
# Чтобы объект красиво выводился.
  def __str__(self):
      return(f'{self.amount} {self.currency}')
    

money1 = Money(100,'USD')
moeny2 = Money(1,'KGS')

print(money1+moeny2)
print(money1-moeny2)
print(money1*2)
print(money1/2)

 


