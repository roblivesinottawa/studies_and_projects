import threading

def function_one():
    for x in range(20):
        print("ONE")

def function_two():
    for x in range(20):
        print("TWO")

t1 = threading.Thread(target=function_one)
t2 = threading.Thread(target=function_two)

t1.start()
t2.start()