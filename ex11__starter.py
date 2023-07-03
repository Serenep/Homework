#!/usr/bin/python

# Assigned variables and used overload * operator to connect the two
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
length = len(Belgium)
hyphen = '\xad'
print(hyphen * length)

print('')
print('')

# used .replace string method to swap comma for colon
print(Belgium.replace(',', ':'))

print('')
print('')

split_Belgium = Belgium.split(',')
population = int(split_Belgium[1]) + int(split_Belgium[3])

message = "The population is {}"
print(message.format(population))

# population = Brussels_pop + Belgium_pop
# used format argument place and a concatenation with addition
# Belgium_pop = 10445852
# Brussels_pop = 737966


