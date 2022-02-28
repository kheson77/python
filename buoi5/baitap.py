from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from abc import ABC, abstractmethod

# Bai1
@dataclass
class BankAccount:
    __id: int
    __name: str
    __balance: float
    # def __init__(self, *, id: int =..., name: str =...,):
    #     self.set_id(id)
    #     self.set_name(name)
    #     self.set_balance(50)
    
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        self.__balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            print('Tai khoan ko du de rut')
        elif amount < 0:
            print('Khong the rut so am')
        else:
            self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount
    
    def transferto(self, account, amount):
        if amount < 0:
            print('Khong the chuyen so am')
            return
        account.amount += amount
        self.balance -= amount
        
    def __len__():
        print('day la len')
    
    def display(self):
        print(f"So du tai khoan la: {self.balance}")
        
# a = BankAccount(1,  2, 30)
# print(a.get_name())
        
# # Bai1 - Kieu 2 
# class BankAccount:
#     def __init__(self, *, id: int =..., name: str =...,):
#         self.id = id
#         self.name = name
#         self.balance = 50
    
#     @property
#     def id(self):
#         return self.__id
    
#     @id.setter
#     def id(self, id):
#          self.__id = id
    
#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, name):
#         self.__name = name
    
#     @property
#     def balance(self):
#         return self.__balance
    
#     @balance.setter
#     def balance(self, balance):
#         self.__balance = balance
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print('Tai khoan ko du de rut')
#         elif amount < 0:
#             print('Khong the rut so am')
#         else:
#             self.balance -= amount
    
#     def deposit(self, amount):
#         self.balance += amount
    
#     def transferto(self, account, amount):
#         if amount < 0:
#             print('Khong the chuyen so am')
#             return
#         account.amount += amount
#         self.balance -= amount
        
#     def display(self):
#         print(f"So du tai khoan la: {self.balance}")
        

# tai_khoan  =BankAccount(id=1, name='123')
# print(tai_khoan.id)

# Bai 2
@dataclass
class SavingsAccount(BankAccount):
    __interest_rate: float
    
    @property
    def interest_rate(self):
        return self.__interest_rate
    
    @interest_rate.setter
    def interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate
    
    def get_lai_suat_1_nam(self):
        return self.get_balance() * self.__interest_rate
        
    
# a = SavingsAccount(1,  2, 30, 1.2)
# print(a.get_lai_suat_1_nam())

# Bai 3
# @dataclass
# class Customers:
#     customer_id: int
#     name: str
#     gender: str
#     dob: datetime
#     contact: str

# @dataclass
# class Bank:
#     name: str = ''
#     accounts: list[BankAccount] = field(default_factory=list) 
#     customers: list[Customers] = field(default_factory=list)
    
#     def openAccount(self, bankAccount: BankAccount):
#         accounts.append(bankAccount)
    
#     def updateAccount(self):
#         for i in self.accounts:
#             i.set_balance(69.9999)
        

# accounts = [
#     BankAccount(1, 'Son', 100),
#     BankAccount(1, 'Son', 100), 
#     BankAccount(1, 'Son', 100),
#     ]

# customers = [
#     Customers(1, 'Son', 'male',  '1999-09-30', '0123456'),
#     Customers(1, 'Thang', 'female','1999-09-30', '0123456'), 
#     Customers(1, 'Nam', 'male', '1999-09-30', '0123456'),
#     ]

# a = Bank('Ngan hang vien thong quan doi', accounts, customers)
# def menu():
#     i = input('[O] OpenAccount ~ [U] UpdateAccount ~ [S] Count of account (Q) Quit: ')
#     i.lower()
#     if(i == 'o'):
#         print('Enter info account')
#         id = input('> id(int)')
#         name = input('> name(name):')
#         balance  = input('> balance(float):')
#         newBank = BankAccount(int(id), str(name), float(balance))
#         a.openAccount(newBank)
#         menu()
#     if(i=='u'):
#         a.updateAccount()
#         menu()
#     if(i=='s'):
#         print(a.accounts[0].get_balance())
#         print(len(a.accounts))
#         menu()
#     if(i=='q'):
#         exit()
        
# menu()



@dataclass
class AWeapon(ABC):
    @abstractmethod
    def attack(self): ...
    
@dataclass
class Gun(AWeapon):
    dame: int
    range: int
    
    def attack(self):
        return self.dame

@dataclass        
class Sword(AWeapon):
    dame: int
    range: int
    
    def attack(self):
        return self.dame
        
class Character:
    def __init__(self, *,name: str, dame: int, heal: int, armor: int, speed: int, weapon: AWeapon):
        self.name = name
        self.dame = dame
        self.heal = heal
        self.armor = armor
        self.speed = speed
        self.mana = 100
        self.timeAttack = 0
        self.weapon = weapon
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
        
    def getDame(self):
        return self.dame
    
    def setDame(self, dame):
        self.dame = dame

    def getHeal(self):
        return self.heal
    
    def setHeal(self, heal):
        self.heal = heal
    
    def getArmor(self):
        return self.armor
    
    def setArmor(self, armor):
        self.armor = armor
    
    def getSpeed(self):
        return self.speed
    
    def setSpeed(self, speed):
        self.speed = speed
    
    def getTimeAttack(self):
        return self.timeAttack
    
    def setTimeAttack(self, timeAttack):
        self.timeAttack = timeAttack
        
    def getMana(self):
        return self.mana
    
    def setMana(self, mana):
        self.mana = mana
        
    def attack(self, enermy: object):
        if(enermy.heal < self.weapon.attack()):
            print(f'{self.name} was killed {enermy.name}!')
            exit()
        elif(self.getTimeAttack() == 2):
            if(self.getMana() >= 20):
                self.setMana(self.getMana() - 20)
                self.setTimeAttack(0)
                print(f'{self.name} use skill, {enermy.name} was x3 Dame!')
                enermy.heal -= self.weapon.attack() * 3
            else:
                enermy.heal -= self.weapon.attack()
        else:
            self.setTimeAttack(self.getTimeAttack() + 1)
            enermy.heal -= self.weapon.attack()
        
def show_info_character():
    if(a.getHeal()==0):
        print(f'{b.name} was killed {a.name}!')
        exit()
    if(b.getHeal()==0):
        print(f'{a.name} was killed {b.name}!')
        exit()
    print("{:<20} {:<10} {:<10} {:<10} {:<10}".format('Name', 'Heal', 'Mana', 'Dame', 'Armor'))
    print("{:<20} {:<10} {:<10} {:<10} {:<10}".format('----------------', '------', '------', '------', '------'))
    print("{:<20} {:<10} {:<10} {:<10} {:<10}".format(a.getName(), a.getHeal(), a.getMana(),a.getDame(), a.getArmor()))
    print("{:<20} {:<10} {:<10} {:<10} {:<10}".format(b.getName(), b.getHeal(), b.getMana(),a.getDame() ,b.getArmor()))
    print("{:<20} {:<10} {:<10} {:<10} {:<10}".format('----------------', '------', '------', '------', '------'))

def choose_menu():
    show_info_character()
    act = input(f"> [1] {a.name} Attack ~ [2] {b.name} Attack ~ (Q) Quit: ")
    act.lower()
    if act == "1":
        print(f'{a.name} attack {b.name}')
        a.attack(b)
        choose_menu()
    elif act == "2":
        print(f'{a.name} attack {b.name}')
        b.attack(a)
        choose_menu()
    elif act == "q":
        exit()
    else:
        print('Syntax error.')
        exit()
    
a = Character(name= "character1", dame = 10, heal = 1000, armor = 100, speed = 100, weapon=Gun(30, 100))
b = Character(name= "character2", dame = 10, heal = 1000, armor = 100, speed = 100, weapon=Sword(40, 10))

choose_menu()

# bvn import List fromtyping