class Vehicle:
    def display_info(self):
        self.make = ""
        self.model = ""
        self.year = ""

class Car(Vehicle):
    def display_info(self):
        self.make = "Mahindra"
        self.model = "XUV 700"
        self.year = 2023
        self.number_of_doors = 4
        return f"\n Car: {self.make} \n Make: {self.model}, \n Year: {self.year}, \n Doors: {self.number_of_doors}"

class Motorcycle(Vehicle):
    def display_info(self):
        self.make = "Hero"
        self.model = "Splendor Pro"
        self.year = 2021
        self.has_sidecar = "Yes"
        return f"\n Motorcycle: {self.make} \n Make: {self.model}, \n Year: {self.year}, \n Sidecar: {self.has_sidecar}"

car_details = Car().display_info()
motorcycle_details = Motorcycle().display_info()

print(car_details)
print(motorcycle_details)
