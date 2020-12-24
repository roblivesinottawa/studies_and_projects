class Customer:
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership


# c = Customer("John", "Gold")
# print(f"{c.name} has a membership of type {c.membership}")

# c2 = Customer("Mary", "Silver")
# print(f"{c2.name} has a membership of type {c2.membership}")

customers = [
    Customer("John", "Gold"),
    Customer("Mary", "Silver")
]

print(f" Customer {customers[0].name} has a membership of type {customers[0].membership}")
print(f" Customer {customers[1].name} has a membership of type {customers[1].membership}")
