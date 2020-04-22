#!/usr/bin/env python2

# This one is like your scripts with argv
def print_two(*args):
  arg1, arg2	= args
  print "arg1: %r, arg2: %r" % (arg1, arg2)

# Ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	  print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one argument
def print_one(arg1):
 print "arg1: %r" % arg1

# This one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Jean-Claude","Clarke")
print_two_again("Jean-Claude","Clarke")
print_one("First!")
print_none()

# NOTE
# code inside functions are identified with indentations
# The industry default is 4 spaces or tab
# It works with different indentations as long as all
# the function code lines have the same indentation. 
# an error will occur if its not
