# Using break, write a program that repeatedly asks the users for some input
# and quits only if the user enters "q" or "Q"

def run():
    while True:
        letter = input("Insert a letter: ")
        if letter.upper() == 'Q':
            break

if __name__ == '__main__':
    run()