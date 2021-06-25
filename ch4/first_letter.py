def main():
    text = input('Tell me your password: ')
    text = text.upper()
    first = text[0]
    return first

if __name__ == '__main__':
    first_letter = main()
    print(f'The first letter you entered was: {first_letter}')