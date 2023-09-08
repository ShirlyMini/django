# multilevel inheritance

# parent--> child1---> child2
# vehicle--->car--->truck
class vehicle:
    def pertolordeisel(self, petrol):
        print(f"It uses {petrol}")

    def price(self, amt):
        print(f"price of the vehicle {amt}")

class car(vehicle):
    def speed(self, kms):
        print(f"speed of the vehicle {kms}")

class truck(car):
    def truck_info(self, name):
        print(f"name of the vehicle {name}")
        self.pertolordeisel("petrol")
        self.price(120000)
        self.speed("120 km/hr")


obj=truck()
obj.truck_info("tata")
obj.pertolordeisel("deisel")

# task

#Hybrid
# 2 multilevel inheritance
    # property1 - vehicle, car, truck (p1)
    # property1 - mobile, apple, samsung ()
# 1 multiple inheritance
    #class userchoice(truck, samsung) - method1 vehicle
                                 #       - method2 mobile