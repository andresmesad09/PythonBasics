def main():
    # First point
    class Dog:
        species = 'Canis familiaris'

        def __init__(self, name, age) -> None:
            self.name = name
            self.age = age

        # Instance method
        def __str__(self) -> str:
            return f'{self.name} is {self.age} years old'

        # Another instance method
        def speak(self, sound):
            return f'{self.name} says {sound}'

    class GoldenRetriver(Dog):
        def speak(self, sound='Bark'):
            return super().speak(sound)

    # Second point
    class Rectangle:

        def __init__(self, lenght, width) -> None:
            self.lenght = lenght
            self.width = width

        def area(self):
            return self.lenght * self.width

    class Square(Rectangle):

        def __init__(self, side_lenght) -> None:
            super().__init__(side_lenght, width=5)

    my_square = Square(4)
    print(my_square.area())


if __name__ == '__main__':
    main()
