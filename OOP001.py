class Person:
    number_of_people = 0 # class attribute (not self)

    def __init__(self, name):
        self.name = name
        Person.number_of_people == 1

p1 = Person("Bill")
print(Person.number_of_people)
p2 = Person("Ted")
print(Person.number_of_people)
