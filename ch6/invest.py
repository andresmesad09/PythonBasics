def invest(amount, rate, years):
    initial_amount = amount
    for i in range(1, years + 1):
        initial_amount = initial_amount + initial_amount * rate
        print(f'year {i}: ${initial_amount:.2f}')


def main():
    amount = float(input('Insert your initial amount: '))
    rate = float(input('Insert the annual rate: '))
    years = int(input('Insert the quantity of years: '))
    invest(amount, rate, years)


if __name__ == '__main__':
    main()
