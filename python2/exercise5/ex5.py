#!/usr/bin/env python2

my_name				= 'Jean-Claude L. Clarke'
my_age				= 38 # not a lie
my_eyes				= 'Brown'
my_teeth			= 'White'
my_hair				= 'Black'
my_height			= 75 # inches
my_weight			= 210 # lbs
my_height_inch		= my_height * 2.54
my_weight_kg		= my_weight * 0.45359237

print "Let's talk about %s." % my_name
print "He's %d inches or %f cm tall." % (my_height, my_height_inch)
print "He's %d pounds or %f kilograms heavy." % (my_weight, my_weight_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
