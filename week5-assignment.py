class Smartphone:
    def __init__(self, brand, model, battery_life):
        # Initializing attributes
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # battery life in percentage

    def display_info(self):
        # Method to display smartphone details
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery Life: {self.battery_life}%")

    def make_call(self, number):
        # Method to simulate making a call
        print(f"Dialing {number}... Call in progress...")

    def charge(self, amount):
        # Method to simulate charging the battery
        if 0 <= self.battery_life + amount <= 100:
            self.battery_life += amount
            print(f"Charging... Battery is now at {self.battery_life}%")
        else:
            print("Error: Battery cannot exceed 100% or go below 0%.")

# Example usage
phone = Smartphone("Apple", "iPhone 13", 50)
phone.display_info()
phone.make_call("123-456-7890")
phone.charge(30)
phone.display_info()


# Activity 2
class Animal:
    def move(self):
        # A generic move method for all animals
        pass

class Dog(Animal):
    def move(self):
        #  Overriding move() for Dog
        print("The dog is running on all fours! 🐕")

class Bird(Animal):
    def move(self):
        # Overriding move() for Bird
        print("The bird is flying through the sky! 🕊️")

class Fish(Animal):
    def move(self):
        # Overriding move() for Fish
        print("The fish is swimming in the water! 🐟")

# Example usage
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()  # Demonstrates polymorphism