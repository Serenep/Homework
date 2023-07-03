# open in read mode
infile = open('pelican.txt', 'r')
# infile.close()

# reads the entire file
print(infile.read())
# Data outputted is a string

# .splitlines returns output as a list
#  len returns the number or items within this list
lines = open('pelican.txt').read().splitlines()
print(lines, len(lines))

with open('pelican.txt', 'r') as infile:
    for line in infile:
        print(line, end='')
infile.close()



