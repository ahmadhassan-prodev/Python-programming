# Syntax of loops is different from java

people = ['Ahmad','Naeem','Ali','Uzair']

for i in people:
    if i=='Ahmad':
        continue
    print(f'current person: {i}')
    if i=='Ali':
        break

for i in range(len(people)):
    print(people[i])

for i in range(-1,12):
    print(f'{i}')

i = 0
while i in range(len(people)):
    print(people[i])
    i += 1