length = int(input("Please, enter an integer representing length: "))
width = int(input("Please, enter an integer representing width: "))
height = int(input("Please, enter an integer representing height: "))

def calculate(l, w, h):
    return l * w * h

print(f"the volume of the rectangular prism is {str(calculate(length, width, height))} cubic feet.")
