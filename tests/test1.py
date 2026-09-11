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
  
    def __init__(self, hero, _balance, __password,bank_name  ):
        self.hero = hero
        self._balance = _balance
        self.__password = __password
        self.bank_name = bank_name
    
    def login(password):
        if password == password:
            return True
        else: return False
    
    def full_info(self):
        print(f'Герой: {self.hero}, Баланс героя: {self.balance} ')

    def get_bank_name(self):
        print(f'{self.bank_name}')
    
    # def bonus_for_level(self):
    #     return self.bonus_for_level
