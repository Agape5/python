
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed  # in km/h

    def move(self):
        print("The vehicle is moving.")

    def __str__(self):
        return f"{self.brand} moving at {self.speed} km/h"

class Car(Vehicle):
    def move(self):
        print(f"{self.brand} is driving on the road at {self.speed} km/h 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"{self.brand} is flying through the sky at {self.speed} km/h ✈️")

class Boat(Vehicle):
    def move(self):
        print(f"{self.brand} is sailing on water at {self.speed} km/h ⛴️")

def travel(vehicle):
    vehicle.move()

if __name__ == "__main__":
    my_car = Car("Toyota", 120)
    my_plane = Plane("Boeing 747", 900)
    my_boat = Boat("Titanic", 45)

    for v in [my_car, my_plane, my_boat]:
        travel(v)
