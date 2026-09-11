# 📝 Домашнее задание №3
# Тема: Инкапсуляция и абстракция в ООП
# 📌 Задание
# Создайте абстрактный класс Hero.
# Для этого используйте модуль:

from abc import ABC, abstractmethod



class Hero(ABC):
# name — имя героя
# level — уровень героя
# __health — здоровье (приватный атрибут)
# strength — сила
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

# 🔹 Методы класса
# 1️⃣ greet()
# Метод выводит сообщение:
# Привет, я {имя героя}, мой уровень {уровень}
    def greet(self):
        print(f'Привет, я {self.name}, мой уровень {self.level}')

# 2️⃣ rest()
# Метод:
# выводит сообщение
# {имя героя} отдыхает
# увеличивает __health на 1
    def rest(self):
        print(f'{self.name} отдыхает')
        self.__health +=1

# 3️⃣ Абстрактный метод attack()
# В родительском классе должен быть абстрактный метод:

    @abstractmethod
    def attack(self):
        pass

 

# Этот метод обязательно должен быть реализован в дочерних классах.
# 📌 Дочерние классы
# Создайте три класса, которые наследуются от Hero:
# Warrior атакует мечом attack()
class Warrior(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)
    
    def attack(self):
        return f'Воин атакует мечом!'
        
# Mage использует магию
class Mage(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)

    def attack(self):
        return f'Маг использует магию!'
    
#Assassin атакует из-под тишка
class Assassin(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)

    def attack(self):
        return f'Assassin атакует из-под тишка!'   

 

 

# 📌 Создать объекты
# Создайте по одному объекту каждого класса:
# Warrior
voin = Warrior('eldar', 10,140, 50)
voin.greet()
voin.attack()
voin.rest()
# Mage
mag = Mage('eldar-mag', 11, 25, 0)
mag.greet()
mag.attack()
mag.rest()
# Assassin
ubiica = Assassin('eldar-ass',9,120,20)
ubiica.greet()
ubiica.attack()
ubiica.rest()
 

# 📌 Вызвать методы
# У каждого героя вызвать:
# greet()
# attack()
# rest()