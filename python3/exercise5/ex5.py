#!/usr/bin/env python3

my_name				= 'Jean-Claude L. Clarke'
my_age				= 38 # not a lie
my_eyes				= 'Brown'
my_teeth			= 'White'
my_hair				= 'Black'
my_height			= 75 # inches
my_weight			= 210 # lbs
my_height_inch		= my_height * 2.54
my_weight_kg		= my_weight * 0.45359237

#for python3, 
# no spaces allowed between f and " when using print 
# This causes a syntax error 
#print(f "hi {name}")
#       ^ this space should is not allowed

print ( f"Let's talk about {my_name}.")
print (f"He's {my_height} inches or {my_height_inch} cm tall.") 
print (f"He's {my_weight} pounds or {my_weight_kg} kilograms heavy.") 
print (f"Actually that's not too heavy.")
print (f"He's got {my_eyes} eyes and {my_hair} hair.")
print (f"His teeth are usually {my_teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total				= my_age + my_height + my_weight
print (f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
