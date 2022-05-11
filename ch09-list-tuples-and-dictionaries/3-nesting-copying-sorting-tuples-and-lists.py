# 1
data = (
    (1, 2),
    (3, 4)
)

# 2
for n, nested in enumerate(data, start=1):
    print(f'Row {n} sum: {sum(nested)}')

# 3
numbers = [4, 3, 2, 1]
print(numbers)

# 4
copy_numbers = numbers[:]
print(copy_numbers)

# 5
numbers.sort()
print(numbers)
