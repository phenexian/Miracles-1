# Filename: wordtolatex.py
import sys
import fileinput


#open("G.txt", "a") as book:

#book.replace(old, new[, count])

filetochange=raw_input("Which file would you like to modify?:")+".txt"


for i, line in enumerate(fileinput.input(filetochange, inplace = 1)):
    sys.stdout.write(line.replace('\n', "\nfor "))
print "The file ",filetochange,"has been modified, with",i, "newlines added"
