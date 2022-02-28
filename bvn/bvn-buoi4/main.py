class Character:
    def __init__(self, *,name: str, dame: int, heal: int, armor: int, speed):
        self.name = name
        self.dame = dame
        self.heal = heal
        self.armor = armor
        self.speed = speed
        self.mana = 100
        self.timeAttack = 0
    
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
        if(enermy.heal < self.dame):
            print(f'{self.name} was killed {enermy.name}!')
            exit()
        elif(self.getTimeAttack() == 2):
            if(self.getMana() >= 20):
                self.setMana(self.getMana() - 20)
                self.setTimeAttack(0)
                print(f'{self.name} use skill, {enermy.name} was x3 Dame!')
                enermy.heal -= self.dame * 3
            else:
                enermy.heal -= self.dame
        else:
            self.setTimeAttack(self.getTimeAttack() + 1)
            enermy.heal -= self.dame
        
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
    
a = Character(name= "character1", dame = 10, heal = 100, armor = 100, speed = 100)
b = Character(name= "character2", dame = 10, heal = 100, armor = 100, speed = 100)

choose_menu()