#!/usr/bin/env python2

from sys import argv

script, filename	= argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want that hit RETURN."

raw_input("?")

print "Opening the file..."
target				= open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I am going to ask for three lines."

line1				= raw_input("line 1: ")
line2				= raw_input("line 2: ")
line3				= raw_input("line 3: ")

print "I am going to print these to the file."
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# extra credit
file_info			= "%s\n%s\n%s\n" % (line1, line2, line3)
target.write(file_info)
# end extra credit

print "And finally, we close it."
target.close()
