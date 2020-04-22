#!/usr/bin/env python2

print "How old are you in years?", #the comma is so that print won't go on a new line
age		= raw_input()
print "How tall are you in cm?",
height	= raw_input()
print "How much do you weigh in lbs?",
weight	= raw_input()

print "So, you're %r years old, %r cm tall, and %r lbs heavy." % (age, height, weight)
