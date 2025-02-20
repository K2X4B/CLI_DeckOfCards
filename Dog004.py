class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print("bark")

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

d0 = Dog("Bill", 4)
d1 = Dog("Ted", 2)

print(d1.get_name())
print(d0.get_age())

d0.set_age(6)
print(d0.get_age())

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade