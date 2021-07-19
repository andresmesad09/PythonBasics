# Catch number of a user. If the user enters something other than integer
# Catch ValueError and displays the message "Try again."

def run():
    while True:
        try:        
            number = int(input("Enter a number: "))
            print(f"Your number is {type(number)} and is {number}")
            break
        except ValueError:
            print("Try again.")


if __name__ == '__main__':
    run()