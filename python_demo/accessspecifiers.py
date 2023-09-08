class vehicle:
    def pertolordeisel(self, petrol):
        print(f"It uses {petrol}")

    # def price(self, amt):
    #     print(f"price of the vehicle {amt}")

    # def __price(self, amt):
    #     print(f"price of the vehicle {amt}")
    #
    # def accesspvt_price(self):
    #     self.__price(123456)

    def _price(self, amt):
        print(f"price of the vehicle {amt}")


class car(vehicle):
    def speed(self, kms):
        print(f"speed of the vehicle {kms}")

class truck(car):
    def truck_info(self, name):
        print(f"name of the vehicle {name}")
        self.pertolordeisel("petrol")
        self._price(120000)
        self.speed("120 km/hr")


obj=truck()
obj.truck_info("Tata")

# obj=vehicle()
# obj.accesspvt_price()