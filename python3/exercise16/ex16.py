#!/usr/bin/env python3

from sys import argv

script, filename	= argv

print ("We're going to erase {filename}")
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you want that hit RETURN.")

input("?")

print ("Opening the file...")
target				= open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I am going to ask for three lines.")

line1		= input("line 1: ")
line2		= input("line 2: ")
line3		= input("line 3: ")

print ("I am going to print these to the file.")
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# extra credit
file_info			= (f"{line1}\n{line2}\n{line3}\n")
target.write(file_info)
# end extra credit

print ("And finally, we close it.")
target.close()
