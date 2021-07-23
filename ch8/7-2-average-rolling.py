"""
Write a program that simulates ten thousand rolls of a fair die and
displays the average number rolled
"""

import random

def run():
    total = 0
    for i in range(10000):
        total += random.randint(1,6)
    return total / 10000
    

if __name__ == '__main__':
    median = run()
    print(f"{median:,.2f}")