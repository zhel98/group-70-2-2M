# 📝 Домашнее задание №2
# Тема: Наследование и полиморфизм в ООП
# 📌 Задание
# Создайте родительский класс Hero, такой же как в прошлом домашнем задании.


# Атрибуты класса Hero
# name — имя героя
# level — уровень героя
# health — здоровье
# strength — сила

class Hero:
    def __init__(self, name, level=1, health=100, strength=100):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength


# Методы класса
# greet() — выводит приветствие
# attack() — герой наносит удар
# rest() — герой отдыхает и восстанавливает здоровье

    def greet(self):
        print('привет!')
    
    def attack(self):
        print('герой наносит удар')
        self.strength -=1
        
    def rest(self):
        print('герой отдыхает')
        self.health +=1

    
# 📌 Создать дочерние классы # 📌 Дополнить конструктор дочерних классов
# От класса Hero должны наследоваться:

# Warrior (Воин)
# добавить атрибут
# stamina — выносливость
# Воин атакует мечом!
class Warrior (Hero):
    def __init__(self, name, level=1, health=100, strength=100, stamina = 100):
        super().__init__(name, level, health, strength)
        self.stamina = stamina
    def attack(self):
        print('воин аттакует мечом!')
        self.stamina -=1
    

# Mage (Маг)
# добавить атрибут
# mana — мана
# Маг кастует заклинание!
class Mage (Hero):
    def __init__(self, name, level=1, health=100, strength=100, mana = 100):
        super().__init__(name, level, health, strength)
        self.mana = mana
    def attack(self):
        print('Маг кастует заклинание!')
        self.mana -=1
      
        
# Assassin (Ассасин)
# добавить атрибут
# stealth — скрытность
#Ассасин атакует из-под тишка!
class Assasin (Hero):
    def __init__(self, name, level=1, health=100, strength=100, stealth = 100):
        super().__init__(name, level, health, strength)
        self.stealth = stealth
    def attack(self):
        print('Ассасин аттакует из-под тишка!')
        self.stealth =0

 
# 📌 Создать объекты
# Создать по одному объекту каждого класса:

# один Warrior
voin = Warrior('Eldar')

# один Mage
mag = Mage('Magichecski Eldar')

# один Assassin
ass = Assasin('IspodTishka Eldar')


# 🎮 Мини-игра "Камень, Ножницы, Бумага"
# Реализовать игровую логику:
# Соответствие героев:
# Warrior  = Камень
# Assassin = Ножницы
# Mage     = Бумага

 
# Логика игры
# 1️⃣ При запуске программы спросить пользователя:
# Выберите героя:
# Warrior / Mage / Assassin
user_choice = input('выберите героя Warrior / Mage / Assassin :').title()
print(f'вы выбрали {user_choice}')


# 2️⃣ После выбора пользователя:
# программа случайно выбирает противника из созданных объектов
import random
enemies = ['Warrior', 'Mage', 'Assassin']
random_enemy = random.choice(enemies)
print(f'противник: {random_enemy}')
 

# 3️⃣ Определяется победитель по правилам:
# Воин побеждает Ассасина
# Ассасин побеждает Мага
# Маг побеждает Воина 

if user_choice == 'Warrior' and random_enemy == 'Assassin':
    print(f'{user_choice} победил')
elif user_choice == 'Assassin' and random_enemy == 'Warrior':
     print(f'{random_enemy} победил')
elif user_choice == 'Assassin' and random_enemy == 'Mage':
    print(f' {user_choice} победил')
elif user_choice == 'Mage' and random_enemy == 'Assassin':
    print(f'{random_enemy} победил')
elif user_choice == 'Mage' and random_enemy == 'Warrior':
    print(f'{user_choice} победил')
elif user_choice == 'Warrior' and random_enemy == 'Mage':
    print(f'{random_enemy} победил')
else:
    print('ничья')
    
 

# 4️⃣ Вывести результат боя:
# Пример:
# Вы выбрали: Warrior
# Противник: Mage
# Mage победил!


# 📦 Что нужно сдать
# 1️⃣ Python файл с решением
# 2️⃣ Залить код на GitHub
# 3️⃣ Отправить ссылку на репозиторий