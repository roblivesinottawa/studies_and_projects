class Person(object):
    population = 100
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18


    def display(self):
        print(f"{self.name} is {self.age} years old")

new_person = Person('Vick', 34)
print(Person.isAdult(23))