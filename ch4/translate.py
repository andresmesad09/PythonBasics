def main():
    user_text = input("Enter some text: ")
    transformed_text = user_text.replace('a', '4')
    transformed_text = transformed_text.replace('b', '8')
    transformed_text = transformed_text.replace('e', '3')
    transformed_text = transformed_text.replace('l', '1')
    transformed_text = transformed_text.replace('s', '5')
    transformed_text = transformed_text.replace('t', '7')
    return transformed_text

if __name__ == '__main__':
    result = main()
    print(result)