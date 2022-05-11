"""
Write a function called roll() that uses randint() to simulate
rolling a fair die by returning a random integer between 1 and 6
"""

import random


def roll():
    random_number = random.randint(1, 6)
    print(random_number)


if __name__ == '__main__':
    roll()
