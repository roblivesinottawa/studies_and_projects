class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}"

    def get_older(self, years):
        self.age += years


person_one = Person('Mike', 30, "lawyer")
person_one.age = 31
print(person_one)
person_two = Person("Ann", 35, "teacher")
print(person_two)


class Worker(Person):
    def __init__(self, name, age, job, salary):
        super(Worker, self).__init__(name, age, job)
        self.salary = salary

    def __str__(self):
        text = super(Worker, self).__str__()
        text += f", Salary: {self.salary}"
        return text

    def calc_annual_salary(self):
        return self.salary * 12


worker_one = Worker("Henry", 40, "programmer", 4000)
print(worker_one)












