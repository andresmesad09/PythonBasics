def convert_cel_to_far(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit


def convert_far_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius


def main():
    fahrenheit = float(input('Enter a temperature in degrees F: '))
    print(f'{fahrenheit:.0f} degrees F = {convert_far_to_cel(fahrenheit):.2f} degrees C\n')
    celsius = float(input('Enter a temperature in degrees C: '))
    print(f'{celsius:.0f} degrees C = {convert_cel_to_far(celsius):.2f} degrees F\n')


if __name__ == '__main__':
    main()
