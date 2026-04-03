# It is used to store key values pairs
Person = {
    'first_name':'Ahmad',
    'last_name':'Hassan',
    'age': 21
}

Person.update({
    'first_name':'Ahmad',
    'last_name':'Hassan',
    'age': 22
    })

# Get value
print(Person)
print(Person['first_name'])
print(Person.get('last_name'))

# Add key/value
Person['Phone#'] = '123456789'
print(Person)

# Get dictionary keys
print(Person.keys())

# Get items
print(Person.items())

# Copy dictionary
Person2 = Person.copy()
Person2['city'] = 'Arifwala'

print(Person2)

# Remove item
del(Person2['last_name'])
Person2.pop('age')
print(Person2)

# List of dict
people = [
    {'name':'Ahmad Hassan','age':21},
    {'name':'Ali Nawaz','age':25}
]

print(people)
print(people[0]['name'])