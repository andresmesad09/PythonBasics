# 8.4 Find the factors of a number

def factors(num):
    for x in range(1, num + 1):
        if num % x:
            continue
        else:
            print(f"{x} is a factor of {num}")


def run():
    num = int(input("Enter a positive integer: "))
    factors(num)


if __name__ == '__main__':
    run()
