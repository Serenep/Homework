
# 'x' is used to create and open a file
# infile = open('pelican.txt', 'x')
# open in read mode
infile = open('pelican.txt', 'r')
# infile.close()

# writing to file with \n to add next output to a new line
output = open('pelican.txt', 'w')
output.write("A wonderful bird is the pelican,\n")
# output.close()

# append to a file using 'a' as 'w' would rewrite whole file
output = open('pelican.txt', 'a')
output.write("His bill holds more than his belican.\n")
# output2.close()

# write list items to different lines terminated ny \n
list = ["He can take in his beak,\n", "Enough food for a week,\n",
"But I'm damned if I see how the helican.\n"]
output.writelines(list)
output.close()




