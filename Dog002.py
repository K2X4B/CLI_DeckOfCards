class Dog:

    def __init__(self, name):
        self.name = name
        
    def bark(self):
        print("bark")

    def get_name(self):
        return self.name

d0 = Dog("Bill")
d1 = Dog("Ted")

print(d1.get_name())
