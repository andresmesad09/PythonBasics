"""
Write a program thtat asks the user to input a string and an integer n, then displays
the character at index n in the string
"""


def run():
    try:
        text = input("Enter some text: ")
        index = int(input("Enter the index you want: "))
        character = text[index]
        print(f"This the character at index {index}: {character}")
    except ValueError:
        print("The index must be an integer")
    except IndexError:
        print(f"The index should be less than {len(text)}")


if __name__ == '__main__':
    run()
