#!/usr/bin/env python3

from sys import argv

script, filename	= argv

txt					= open(filename)

print (f"Here's your file {filename}")
print (txt.read())

print ("Type the file name again:")
file_again			= input("> ")

txt_again			= open(file_again)

print (txt_again.read())

# NOTE
# You can run "python 3.6" in the terminal to get a python terminal.
# There you can run the following just like in this exercise.
# file = "blah"
# text = open(file)
# text.read()
# It will execute like running this file.
