# REVIEW OOP, classes, constructor
# classmethod, staticmethod

class Ninja:
    # belong to the Class - NOT the instance
    all_ninjas = [] # not part of the constructor / no self
    
    # constructor
    def __init__(self, name, health, age, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
        # self.weapon = Weapon(22, "any", "bubble")
        if Ninja.check_age(age):
            self.age = age
        else:
            return
        Ninja.all_ninjas.append(self)
    
    # methods-------
    def display_stats(self):
        print("stats: " + self.name + " has " + str(self.health) + " hp")
       
    def eat_strawberry(self):
        self.health = self.health + 10
        print(f"{self.name} ate a strawberry and they now have {self.health} ")
        # return "ok"
        
    def attack(self, enemy_ninja):
        # print(f"{self.name} is attacking {enemy_ninja.name}")
        enemy_ninja.health -= self.weapon.damage
        print(f"{self.name} used a {self.weapon.name} which deals {self.weapon.damage} dmg")
        print(f"{enemy_ninja.name} gets attacked by {self.name} with {self.weapon.damage} dmg\n they now have {enemy_ninja.health}")
        
    #? Class methods
    """
    do not have access to the instance
    no self
    they do not individually change any one instance
    can only be called from the Class
    """
    
    @classmethod
    def party(cls):
        print(len(cls.all_ninjas))
        # print(cls.all_ninjas[1].name)
        for one_ninja in cls.all_ninjas :
            one_ninja.eat_strawberry()
            
        # print(Ninja.all_ninjas)
    
    # ? static methods
    """
    stationary / non-changing
    no access to anything
    independent
    # utility and validations
    """
    @staticmethod
    def check_age(age):
        is_valid = True
        if age < 18:
            is_valid = False
            print("you are not old enough to enter the dojo")
        return is_valid
    
    @staticmethod
    def add(num1, num2):
        return num1 + num2

# ----------- other class--------------
class Weapon:
    def __init__(self, data, durability=100):
        self.damage = data['damage']
        self.type = data['type']
        self.name = data['name']
        self.durability = durability
    
katana ={
    "damage": 20,
    "type" : "melee",
    "name" :"katana",
}
lasers ={
    "damage": 200,
    "type" : "range",
    "name" :"laz0rs",
}

weapon1 = Weapon(lasers)
# weapon2 = Weapon(5, "range", "crossbow")

ninja1 = Ninja("Michael Angelo", 100, 19, weapon1)
ninja2 = Ninja("Naruto", 50, 18, katana)

ninja1.attack(ninja2)


# ninja2 = Ninja("dude", 100, 10, "stick")
Ninja.party()


# print(Ninja.all_ninjas)

# ninja2.display_stats()
# ninja1.attack(ninja2)
# ninja2.display_stats()



# print(ninja1.name)
# ninja1.display_stats()
# ninja1.eat_strawberry()
# ninja1.eat_strawberry()
# ninja1.eat_strawberry()
# ninja1.display_stats()


# ninja2.eat_strawberry()
# ninja2.display_stats()