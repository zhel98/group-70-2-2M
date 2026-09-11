class Hero():
    def __init__ (self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    
    def action(self):
        print(f'{self.name} готов к бою')

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mana):
        super().__init__(name, lvl, hp)
        self.mana = mana
    
    def action(self):
        print(f'{self.name} кастует заклинание! MP: {self.mana}')

class WarriorHero(MageHero): #не хватает атрибута маны
    def __init__(self, name, lvl, hp, mana=0):
        super().__init__(name, lvl, hp, mana)
        
    def action(self):
        print(f'{self.name} рубит мечом! Уровень {self.lvl}')
        
class BankAccount():
    bank_name = 'Optima'
    
    def __init__(self, hero, _balance, __password ):
        self.hero = hero
        self._balance = _balance
        self.__password = __password
  
    
    def login(self, password):
        if password == self.__password:
            return True
        else:
            return False
    
    @property
    def full_info(self):
        print(f'Герой: {self.hero}, Баланс героя: {self.balance} ')

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name
    
    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f'{self.hero.name} | Balans: {self._balance} SOM'
    
    def __add__(self, other):
        if type(self.hero) is type(other.hero):
            return self._balance + other._balance
        else:
            print('Нельзя прибавлять баланс разных персонажей')
    
    def __eq__(self, other):
        if type(self.hero) == type(other.hero) and self.hero.lvl == other.hero.lvl:
            return True
        else: return False

 #Создаем героев
hero1 = MageHero("Merlin", 5, 100, 150)
hero2 = MageHero("Gandalf", 0, 120, 200)
hero3 = WarriorHero("Conan", 1, 200)

# Вызываем метод action для демонстрации
hero1.action()
hero3.action()

# Создаем банковские счета
acc1 = BankAccount(hero1, 5000, "pass123")
acc2 = BankAccount(hero2, 3000, "pass456")
acc3 = BankAccount(hero3, 4000, "pass789")

print(acc1)
print(acc2)

print("Банк:", BankAccount.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

# --- Магические методы: __add__ ---
print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)
print("Сумма мага и воина:", acc1 + acc3)

# --- Магический метод: __eq__ ---
print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)  # True — одинаковый класс и уровень
print("Mage1 == Warrior ?", acc1 == acc3)  # False