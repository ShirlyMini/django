# Hierarchical inheritance
# one parent multiple child

class vehicle:# ----Parent
    def pertolordeisel(self, petrol):
        print(f"It uses {petrol}")

    def price(self, amt):
        print(f"price of the vehicle {amt}")

class car(vehicle):
    def speed(self, kms):
        print(f"speed of the car {kms}")

class cycle(vehicle):
    def speed(self, kms):
        print(f"speed of the cycle {kms}")

class truck(vehicle):
    def truck_info(self, name):
        print(f"name of the vehicle {name}")
        self.pertolordeisel("petrol")
        self.price(120000)

obj=truck()
obj.truck_info("tata")

obj1=car()
obj1.speed("120")

obj2=cycle()
obj2.speed("20")