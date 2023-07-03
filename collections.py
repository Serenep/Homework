

# string with an item value
someString =  'Norwegian Blue', 'Mr. Kahns bike'


# collection - list with items
fruitList = ['Banana', 'Apples', 'Guava', 'Oranges']
numberList = [3, 5, 7, 9, 1]

print('min:', min(numberList))
print('max:',max(numberList))
print('sum:', sum(numberList))

print("")
print("")

# access individual items using their idexes
print(numberList[0])
print(numberList[2])

# length of a list
print("Length of the list is", len(numberList))

# return a range of items from a list - start index (included) to end index (excluded)
print(numberList[1:3])

print("")
print("")


# get items from beginning of list to a position
print(numberList[:3])
print(numberList[3:])

print("")
print("")

# change items
numberList[0] = 90
numberList[3:]=[50,50]

print(numberList)

print("")
print("")


# add items to a list
fruitList += ['Mangoes', 'Pineapple']
print(fruitList)

# remove items
fruitList.remove('Mangoes')

# iterate or loop over our list
for fruit in fruitList:
    print(fruit)

#
count = fruitList.count('Pineapple')
print("Mangoes occur", count, "time(s)")

# find the index of an item
fruitList.index('Pineapple')

# find the index of a non-existing item - cars not in item so wont find
# fruitList.index(cars)

# sort list items
fruitList.sort()
print(fruitList)
fruitList.sort(reverse=True)
print(fruitList)

print("")
print("")

# dictionaries
# key-value pairs-enter key return value
mydict = {'Australia':'Canberra', 'Eire':'Dublin', 'France':'Paris'}
print(mydict['Australia'])

country = 'Iceland'
mydict[country] = 'Reykjavik'
print(mydict['Iceland'])

print("")
print("")

# dictionary storing an object or type of list with keys and values
mydict2 = {'UK':['London', 'Wigan', 'Manchester'], 'US':['Miami','New York', 'Boston']}
print(mydict2['UK'][2])

mydict2['FR'] = ['Paris', 'Lyon', 'Bordeaux']
print(mydict2['FR'][2])

for item in mydict2:
    print(mydict2[item])

print("")
print("")

foods = ['Pizza', 'Kebab', 'Chinese', 'Burgers', 'Chips']
for item in foods:
     print()

most_letters = 0
most_letters_item = None
for letters in foods:
    if len(letters) > most_letters:
        most_letters = len(letters)
        most_letters_item = letters
print(most_letters_item)
print(most_letters)

fruits = ["apple", "banana",  "watermelon", "pineapple"]
longest_fruit = ""
max_characters = 0
for fruit in fruits:
    if len(fruit) > max_characters:
        longest_fruit = fruit
        max_characters = len(fruit)
print("Fruit with the longest name:", longest_fruit)
print("Number of characters:", max_characters)

















