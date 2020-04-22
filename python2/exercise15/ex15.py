#!/usr/bin/env python2

from sys import argv

script, filename	= argv

txt					= open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the file name again:"
file_again			= raw_input("> ")

txt_again			= open(file_again)

print txt_again.read()

# NOTE
# You can run "python 2.7" in the terminal to get a python terminal.
# There you can run the following just like in this exercise.
# file = "blah"
# text = open(file)
# text.read()
# It will execute like running this file
