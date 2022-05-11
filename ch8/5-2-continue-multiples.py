# Using continue, write a programthat loops over the numbers
# 1 to 50 and print all numbers that are not multiples of 3

def run():
    for i in range(1, 51):
        if i % 3:
            print(i)


if __name__ == '__main__':
    run()
