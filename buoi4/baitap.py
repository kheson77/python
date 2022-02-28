
from math import pi
from dataclasses import dataclass

# Bai1
# class BankAccount:
#     def __init__(self, *, id: int =..., name: str =...,):
#         self.id = id
#         self.name = name
#         self.balance = 50
    
#     def get_id(self):
#         return self.id
    
#     def get_name(self):
#         return self.name
    
#     def get_balance(self):
#         return self.balance
    
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
       
       
# son = BankAccount(id =1, name='Son') 
# print(son.deposit(100))
# print(son.display())

# Bai2
# pi = 3.14
# class Circle:
#     def __init__(self, *, radius: float):
#         self.radius = radius
    
#     def get_radius(self):
#         return self.radius
    
#     def set_radius(self, radius):
#         self.radius = radius
#         return
    
#     def find_area(self):
#         D = (self.radius * 2)
#         return D*D*pi/4
    
#     def find_circumference(self):
#         D = (self.radius * 2)
#         return D*pi
    
#     def __add__(self, __o: object):
#         if not isinstance(__o, Circle):
#             raise TypeError(f"{__o.__class__} are not support")
#         else:
#             x = self.radius + __o.radius
#             return Circle(radius=x)
    
#     def __sub__(self, __o: object):
#         if not isinstance(__o, Circle):
#             raise TypeError(f"{__o.__class__} are not support")
#         else:
#             x = self.radius - __o.radius
#             return Circle(radius=x)
    
#     def __eq__(self, __o: object):
#         if not isinstance(__o, Circle):
#             raise TypeError(f"{__o.__class__} are not support")
#         else:
#             if self.radius == __o.radius:
#                 return True
#             else:
#                 return False
            
#     def __lt__(self, __o: object):
#         if not isinstance(__o, Circle):
#             raise TypeError(f"{__o.__class__} are not support")
#         else:
#             if self.radius < __o.radius:
#                 return True
#             else:
#                 return False
    
#     def __gt__(self, __o: object):
#         if not isinstance(__o, Circle):
#             raise TypeError(f"{__o.__class__} are not support")
#         else:
#             if self.radius > __o.radius:
#                 return True
#             else:
#                 return False
    
#     def display(self):
#         print(f"Ban kinh hinh tron la: {self.radius}")
        
# a = Circle(radius = 10)
# b = Circle(radius = 24)

# print((b-a).find_area())
# print(a < b)

# bai3
@dataclass(order=True)
class Rectangle:
    length: float
    width: float
    # def __init__(self, *, length, width):
    #     self.length = length
    #     self.width = width
    
    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
    
    def set_length(self, length):
        self.length = length
        
    def set_width(self, width):
        self.width = width
        
    def find_area(self):
        a = self.width
        b = self.length
        return (a+b)*2
        
    def find_circumference(self):
        a = self.width
        b = self.length
        return a*b
    
    def display(self):
        print(f"Ban kinh hinh tron la: {self.radius}")

hcn1 = Rectangle(length = 10,width= 20)
hcn2 = Rectangle(length = 10,width= 21)

print(hcn1.width + hcn2.width)
print(hcn1.find_circumference())