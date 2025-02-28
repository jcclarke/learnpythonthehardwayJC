#!/usr/bin/env python2

# Create a mapping of state to abbreviation
states			= {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# Create a basic set of states and some cities in them
cities			= {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# Add some more cities
cities['NY']	= 'New York'
cities['OR']	= 'Porland'

# Print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# Print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# Do it by using the state then cities dictionary
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# Print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# Print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city of %s" % (abbrev, city)

# Now print both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s and has the city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviated state that might not be there
state			= states.get('Texas', None)

if not state:
	print "Sorry, no Texas."

# get  city with a default value
city			= cities.get('TX', 'not exisTant!')
print "The city for the state of 'TX' is: %s" % city
