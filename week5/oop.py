# Assignment 1: Design Your Own Class 

class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery  # private (encapsulation)

    def call(self, number):
        return f"Calling {number} from {self.model}..."

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        return f"⚡ {self.model} charged to {self.__battery}%"

    def get_battery(self):
        return f"Battery level: {self.__battery}%"

# Inheritance Example
class GamingPhone(Smartphone):
    def play_game(self, game):
        return f"Playing {game} on {self.model} with high graphics mode!"


# Activity 2: Polymorphism Challenge 

class Car:
    def move(self):
        return "Driving on the road"

class Plane:
    def move(self):
        return "Flying in the sky"

class Boat:
    def move(self):
        return "Sailing on water"


# -------------------------
# Testing the Program
# -------------------------

# Assignment 1 Demo
phone1 = Smartphone("Samsung", "S23", 50)
print(phone1.call("0712345678"))
print(phone1.charge(30))
print(phone1.get_battery())

gaming = GamingPhone("Asus", "ROG Phone 6", 70)
print(gaming.play_game("PUBG"))
print(gaming.get_battery())

print("\n--- Polymorphism Challenge ---")

# Activity 2 Demo
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    print(v.move())
