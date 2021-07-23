import random

def coin_flip():
    coin_result = random.randint(0, 1)
    if coin_result == 0:
        return 'heads'
    else:
        return 'tails'

def run():
    
    flips = 0
    trials = 10000

    for trial in range(trials):
        if coin_flip() == 'heads':
            flips += 1
            while coin_flip() == 'heads':
                flips += 1
            flips += 1
        else:
            flips += 1
            while coin_flip() == 'tails':
                flips += 1
            flips += 1
    
    avg_flips = flips / trials
    return avg_flips


if __name__ == '__main__':
    average = run()
    print(f"Average of flips to get both heads and tails: {average:.0f}")