# inheritance

class Vehicle:
    def drive(self):
        return "drive"


class Truck(Vehicle):
   def offroad(self):
       return "Trucks drive well in the mud and hard terrain"


class Sedan(Vehicle):
    def city(self):
        return "Sedans drive well in city environments"


car_one = Truck()
print(car_one.offroad())
car_two = Sedan()
print(car_two.city())