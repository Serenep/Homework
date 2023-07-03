import os

# open in read mode
infile = open('myfile.txt', 'r')
infile.close()

# reads the entire file
# print(infile.read())

print("")
print("")

# readline
infile2 = open('myfile.txt', 'r')
line = infile2.readlines()
print(line)
infile2.close()

# read the whole file
lines = open('myfile.txt').read()
print(lines)

# returns text as list
lines = open('myfile.txt').read().splitlines()
print(lines)

with open('myfile.txt','r') as infile:
    for line in infile:
        print(line,end='')

print("")
print("")

infile = open('myfile.txt', 'r')
print(infile)

# writing to file - write rewrites whole file
output = open('myfile.txt', 'w')
output.write("7\n")
output.close()

# append to a file
output2 = open('myfile.txt', 'a')
output2.write("7\n")
output2.close()

# write list items to different lines terminated ny \n
# fruits = ['oranges\n', 'mangoes\n']
# output2.writelines(fruits)
# output2.close()

# same line
fruits = ['oranges', 'mangoes']
output2.writelines(fruits)
output2.close()

# for fruit in fruits:
#     output2.write(fruit)
#     output2.write("\n")


output2.write("pineapple, banana")
output2.close()


os.remove('myfile.txt')














