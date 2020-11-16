class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"



vector_one = Vector(2,5)
vector_two = Vector(6,3)
print(vector_one)
print(vector_two)

vector_three = vector_one + vector_two
print(vector_three)