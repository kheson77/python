# class People:
#     """Model for the dog in real life"""
    
#     # Sau dau * bat buoc phai truyen cac thuoc tinh
#     def __init__(self, *, name: str =..., age: int =..., color: str =...):
#         self.name = name
#         self.age = age 
#         self.color = color
    
#     def sleep(self, hours: int = ...):
#         print(f"{self.name} sleep in {hours}h")
    
#     def attach(self, instance: str = ...):
#         print(f"{self.name} attach {instance}")
    
#     def jump(self, height: int = ...):
#         print(f"{self.name} jump in {height}m")
        
#     @classmethod
#     def fromdict(cls, data):
#         return cls(**data)
    
# con_nguoi = People(name = "Con cho",age =  12,color= "red")

# print(con_nguoi.attach('Con nguoi'))
# print(con_nguoi.sleep(10))

# Son = People.fromdict({"name": "Sam", "age": 2, "color": "Yellow"})



class Point:
    """Con tro chuot"""
    def __init__(self, *, x: int =..., y: int =...):
        self.x = x
        self.y = y 
        
    def display(self):
        print(f"Display x with Offset({self.x},{self.y})")
        
    def move(self, *, toX, toY):
        print(f"Move to Offset({toX},{toY})")
        
    @classmethod
    def zero(cls):
        return cls(x=0,y=0)
    
point1 = Point.zero()
point2 = Point(x=10, y=20)
print(point1.display())
print(point2.display())
