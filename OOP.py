class Person:
    number_of_people = 0 # class attribute (not self)

    def __init__(self, name):
        self.name = name

p1 = Person("Bill")
p2 = Person("Ted")

Person.number_of_people = 8
print(p2.number_of_people)