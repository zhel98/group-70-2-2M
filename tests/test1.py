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

class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp):
        super().__init__(name, lvl, hp)
        
    def action(self):
        print(f'{self.name} рубит мечом! Уровень {self.lvl}')
        
class BankAccount():
    bank_name = 'Optima'
    def __init__(self, hero, _balance, __password ):
        self.hero = hero
        self._balance = _balance
        self.__password = __password
  
    
    def login(password):
        if password == password: return True
        else: return False
    
    @staticmethod
    def full_info(self):
        print(f'Герой: {self.hero}, Баланс героя: {self.balance} ')

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name
    
    # def bonus_for_level(self):
    #     return self.bonus_for_level
    
    def __str__(self):
        return f'{self.get_bank_name} | {self._balance} SOM'
    
    def __add__(self, other):
        if type(self) is type(other):
            return self.__class__(self._balance + other._balance)
        else:
            print('Нельзя прибавлять баланс разных персонажей')
    
    def __eq__(self, other):
        if self.full_info.