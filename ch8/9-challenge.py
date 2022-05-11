import random


def a_wins(prob):
    """Return True of a regional election, either True or False.

    The chances of A winning are determined by prob.    
    """
    if random.random() < prob:
        return True
    else:
        return False


def run():

    elections = 10000
    candidate_a_wins = 0

    for election in range(elections):
        # Return true if A wins, false otherwise
        region_1 = a_wins(0.87)
        # Return true if A wins, false otherwise
        region_2 = a_wins(0.65)
        # Return true if A wins, false otherwise
        region_3 = a_wins(0.17)
        # We sum the results (booleans can be summarized).
        total = region_1 + region_2 + region_3
        if total >= 2:
            candidate_a_wins += 1
        else:
            continue

    percentage = (candidate_a_wins / elections) * 100
    print(f"The percentage of times in which candidate A wins is: {percentage:.2f}")


if __name__ == '__main__':
    run()
