# It is like lists but it does not allow duplicate values

fruits = {'Apple','Orange', 'Bnana', 'Grapes'}

# check if in set
print('Grapes' in fruits)

# Add value
fruits.add('Mango')

print(fruits)

# Remove value
fruits.remove('Bnana')
print(fruits)

# Clear set
fruits.clear()
print(fruits)

# Delete set
del fruits
print(fruits)