#!/usr/bin/env python2

## Animal is-a object (yes, sort of confusing) look at the exit criteria
class Animal(object):
	pass

## Dog is-a animal that has-a __init__ that take parameters self, and name
class Dog(Animal):
	
	def __init__(self, name):
		## Dog has an attribute called name
		self.name	= name

## Cat is-a Animal that has-a __init__ that take parameters self, and name
class Cat(Animal):
	
	def __init__(self, name):
		## Cat has-a attribute called name
		self.name	= name

## Person is-a object that has-a __init__ that take parameters self, and name
class Person(object):
	
	def __init__(self, name):
		## Person has-a name attribute
		self.name	= name

		## Person has-a pet of some kind
		self.pet	= None

## Employee is-a Person that has-a __init__ that takes parameters self, name, and salary
class Employee(Person):
	
	def __init__(self, name, salary):
		## Calls the Person class to inherit it's __init__ function. hmmm, what is this strange magic?
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary	= salary		

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish 
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass


## rover is-a Dog
rover		= Dog("Rover")

## Satan is-a Cat
satan		= Cat("Satan")

## Mary is-a Person
mary		= Person("Mary")

## Mary has-a pet cat called Satan
mary.pet	= satan

## Frank is-a Employee that has-a 120000 salary
frank		= Employee("Frank", 120000)

## Frank has-a pet dog called Rover 
frank.pet	= rover

## flipper is-a Fish
flipper		= Fish()

## crouse is-a Salmon
crouse		= Salmon()

## Harry is-a Halibut
harry		= Halibut()

print mary.name, "\t", mary.pet.name
print frank.name, "\t", frank.pet.name, "\t", frank.salary
