# Ceate a list named food with two elements, rice and beans
food = ['rice', 'beans']
print(food)

# Append the string 'broccoli' to food using .append()
food.append('broccoli')
print(food)

# Add the strings bread and pizza to food using .extend()
food.extend(['bread', 'pizza'])
print(food)

# print the first two items in the food list using print and slice notation
print(food[:2])

# Print the last item in food using print and index notation
print(food[-1])

# Create a list called breakfast from the strings eggs, fruit, orange juice using the .split() method
breakfast = 'eggs, fruit, orange juice'.split(',')
print(breakfast)

# Verify that breaksfast has three items using len()
print(f'Does breakfast have three items? {len(breakfast) == 3}')

# Create a new list called lengths using list comprehension that contains the lengths of each string in the breakfast list
lengths = [len(item) for item in breakfast]
print(lengths)  