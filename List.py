# Lists are like arrays 

numbers = [1,3,4,4,5]

print(numbers)
print(numbers[3])

print(len(numbers))

# Method to add value in a list
fruits = []

fruits.append('Mangos')
fruits.append('Apple')
fruits.append('Orange')
fruits.append('Banana')

print(fruits)

# Method to remove value from list

fruits.remove('Apple')

print(fruits)

# Method to insert value in particular position

fruits.insert(2, "Strawberies")

print(fruits)

# Remove values from particular position

fruits.pop(1)

# To reverse list

fruits.reverse()
print(fruits)

# Arrange list in alphabetical order

fruits.sort()
print(fruits)

# Arrenge list in reverse aplhabetic order

fruits.sort(reverse=True)
print(fruits)

# To change values

fruits[2] = 'Grapes'
print(fruits)