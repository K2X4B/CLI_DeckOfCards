class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")

class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Bill", 9)
p.show()
c = Cat("Ted", 4)
c.speak()
d = Dog("Death", 25000)
d.speak()
f = Fish("Bubbles", 2)
f.speak()