# OOP

# ? objects?
# an instance of a class

# ? class?
# template or blueprint for our instances(objects)

dog1 = {
    'name' : 'Spot',
    'age' : 4,
    'breed' : 'malti poo'
}

dog2 = {
    'name' : 'Buddey',
    'age' : 6,
    'breed' : 'black lab'
}
# print(dog2['name'])
# class User:
#     pass

# ---------- CREATE A CLASS ------------
class Dog:
    # constructor - creates defaults and builds the class
    def __init__(self, name_param, age, breed="lab"):
        # ? attributes
        self.breed = breed
        self.name = name_param
        self.age = age
        # print(self)
    
    #? --- methods ---
    def bark(self):
        print(f"{self.name} makes a loud bark!!!!!!")
        return self
    
    def birthday(self):
        # self.age = self.age + 1
        self.age += 1
        print(f"{self.name} gets a year older, and they are now {self.age}")
        return self
    
    # __main__ = it ran directly from the file
    # __repr__ = overwrites the <__main__.Dog object at 0x00001544556>
    # string representation of the instance
    def __repr__(self):
        return f"{self.name} is a {self.breed}"

# --- instantiate the class -> create objects form the blueprint
doggo1 = Dog("Courage", 8)
# print(doggo1)


doggo2 = Dog( age=10, name_param="rex", breed="german shepard")

# doggo1.bark()
# doggo2.bark()

print(doggo1.birthday())
doggo1.birthday().bark().birthday()

doggo2.birthday()
doggo2.birthday()
doggo2.birthday()

# doggo2.name
# doggo2.age


# print(f"{doggo1.name} is a {doggo1.breed}")