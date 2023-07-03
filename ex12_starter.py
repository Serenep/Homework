import random

# What is wrong with this?
# += operator is used to add items to end of list with []
# To add a single item you would usually use append method

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'
cheese.append('Oke')
print(cheese)

# What is going on here? Can you explain the output?

tup = 'Hello'
print(len(tup))

# Trailing commas at end of lists or tuples and makes item more readable and a single item
tup = 'Hello',
print(len(tup))


# Lotto
# randomlist is an empty list
# Imported random and used with .randint(1,50) to generate random numbers between 1 & 50
# used a for loop with a range of 6 and .append to add each iteration to the list
# printed is a random 6 number lottery generator/appended list

randomlist = []
for i in range(0, 6):
  x = random.randint(1, 50)
  randomlist.append(x)
print(randomlist)



