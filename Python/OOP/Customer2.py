class User:
    def log(self):
        print(self)

class Teacher(User):
    def log(self):
        print("This is a teacher")

class Customer(User):
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership

    # creating properties
    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
        self._name = name

    def update_membership(self, new_membership):
        self.membership = new_membership

    def __str__(self):
        return f" Customer {self.name} has a membership of type {self.membership}"


    def __eq__(self, other):
        if self.name == other.name and self.membership == other.membership:
            return True
        return False


    __hash__ = None

    __repr__ = __str__


users = [
    Customer("John", "Gold"),
    Customer("Mary", "Silver"),
    Teacher()
]

# print(customers[0] == customers[1])
# print(customers)
# customers[2].log()

for user in users:
    user.log()

