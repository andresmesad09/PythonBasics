class Dog:
    species = 'Canis familiaris'

    def __init__(self, name, age, coat_color) -> None:
        self.name = name
        self.age = age
        self.coat_color = coat_color

    # Instance method
    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old. And has a {self.coat_color} coat'

    # Another instance method
    def speak(self, sound):
        return f'{self.name} says {sound}'


miles = Dog('miles', 4, 'blue')
print(miles)


class Car:
    def __init__(self, color, mileage) -> None:
        self.color = color
        self.mileage = mileage

    def __str__(self) -> str:
        return f'The {self.color} has {self.mileage:,} miles.'

    def drive(self, miles):
        self.mileage += miles


# Instantiating two car objects
blue_car = Car('blue', 20000)
red_car = Car('red', 30000)
new_car = Car('grey', 0)

print(f"The new car before being modified \n{new_car}")
new_car.drive(100)
print(f"The new car after being modified \n{new_car}")
new_car.drive(100)
print(f"The new car after drive another 100 miles \n{new_car}")
