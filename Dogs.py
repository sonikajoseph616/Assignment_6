class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"\nDog Name: {self.name}\nDog Age: {self.age} years")

    def get_info(self):
        print("Dog Coat color:", self.coat_color)

class Shihtzu(Dog):
    def pet(self):
        print("He is a Pet dog")

    def non_veg_food(self):
        print("Non-veg food is favorite")

class Husky(Dog):
    def run(self):
        print("Runs very fast")

    def bark(self):
        print("Barks loudly")


# Create instances of the dog breeds
Oreo = Shihtzu("Oreo", 2, "Golden and Brown")
Laska = Husky("Laska", 5, "White and Black")

# Call methods on the instances
Oreo.description()
Oreo.get_info()
Oreo.pet()
Oreo.non_veg_food()

Laska.description()
Laska.get_info()
Laska.run()
Laska.bark()
