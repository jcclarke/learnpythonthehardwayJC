#!/usr/bin/env python2

from sys import exit

hp			= 100
food		= 50
attack		= 50
damage		= 25
monster		= 400
knife		= 50
game_stats	= [hp, food, attack, damage, monster, knife]
find_knife	= False
key			= False
find_food	= False

def gold_room():
	print "This room is full of gold. How much do you take?"

	next			= int(raw_input("> "))
	if int(next) != 0:
	#if "0" in next or "1" in next:
		how_much	= int(next)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You gready bastard!")


def hall_room():
	print "The bear is here and he has a bunch of honey."
	print "The fat bear is blocking your path to both doors."
	print "How are you going to move the bear?"
	print "You can \n(1) take honey \n(2) taunt bear \n(3) try and open door on the left\n(4) try and open door infront\n"
	bear_moved		= False

	while True:
		next		= int(raw_input("> "))

		if next == 1:
			print "You try and take the honey.\n"
			dead("The bear looks at you and slaps your face off!")
		elif next == 2 and not bear_moved:
			print "You taunt the bear."
			print "The bear has moved from your path.\nYou can go through a door now.\n"
			bear_moved	= True
		elif next == 2 and bear_moved:
			print "You taunt the bear again.\n"
			dead("The bear gets pissed off and chews your leg off!")
		elif next == 3 and bear_moved:
			print "You open the door on the left\n"
			print "---\nYou enter the Living room!\n---\n"
			living_room()
		elif next == 4 and bear_moved:
			print "You open the door infront\n"
			print "---\nYou enter the Throne room!\n---\n"
			throne_room()
		elif (next == 3 or next == 4) and not bear_moved:
			print "You try and open a door.\n"
			dead("The bear attacks you and you get Mauled!")
		else:
			print "I got no idea what that means."


def throne_room():
	print "There is a monster here."
	print "He is blocking the door to the Gold room behind the throne."
	print "There is also a door to the left and a door behind."
	print "What will you do?"
	print "(1) attack monster \n(2)open Gold room door \n(3)flee through left door \n (4)flee through door behind\n"

	#global hp, monster
	global game_stats

	while True:
		next		= int(raw_input("> "))

		if next == 1 and game_stats[4] <= 0:
			print "The monster is dead.\nThere is nothing to attack!!!\n"
		elif next == 1:
			game_stats[0]	-= game_stats[3]
			game_stats[4]	-= game_stats[2]
			print "You attacked the Monster!\n"
			if game_stats[0] <= 0 and game_stats[4] <= 0:
				dead("DOUBLE KO!!!!  :o\nYou killed the monster but you died in the in the process!")
			elif game_stats[0] <= 0:
				dead("YOU DIED!!!\nThe monster killed you.    :(")
			elif game_stats[4] <= 0:
				print "\nYOU DEFEATED THE MONSTER!!\n"
			else:
				print "HP = %d\nmonster HP = %d\n" % (game_stats[0], game_stats[4])
		elif next == 2 and game_stats[4] > 0:
			game_stats[0]	= game_stats[0] - 2 * game_stats[3]
			print "You tried to open the Gold room door\nThe monster attacks you!"
			print "HP = %d\nmonster HP = %d\n" % (game_stats[0], game_stats[4])
			if game_stats[0] <= 0:
				dead("YOU DIED!!!\nThe monster killed you.    :(")
		elif next == 2 and game_stats[4] <= 0:
			print "After killing the monster, you open the door infront\n"
			print "---\nYou enter the GOLD room!\n---\n"
			gold_room()
		elif next == 3:
			print "You open the door to your left and flee from the monster"
			print "---\nYou enter the Kitchen!\n---\n"
			kitchen_room()
		elif next == 4:
			print "You open the door behind you and flee from the monster"
			print "---\nYou enter the Great Hall!\n---\n"
			hall_room()
		else:
			game_stats[0]	-= game_stats[3]
			print "You do nothing!\nThe monster attacks you!"
			print "HP = %d\nmonster HP = %d\n" % (game_stats[0], game_stats[4])
			if game_stats[0] <= 0:
				dead("YOU DIED!!!\nThe monster killed you.    :(")


def kitchen_room():
	print "There are lots of dirty dishes here"
	print "And there are also some cupboards"
	print "You also see 3 doors"
	print "(1) clean the dishes\n(2) search the cupboards\n(3) go through the door on the left"
	print "(4) go through the door to the right\n(5) go through the door behind you\n"

	global game_stats, find_food

	while True:
		next		= int(raw_input("> "))

		if next == 1:
			print "You cleaned some dishes\nYou feel good about yourself.  :)"
		elif next == 2 and not find_food:
			game_stats[0]	+= game_stats[1]
			find_food		= True
			print "You search the cupboard and find some food\nHP = %d\n" % game_stats[0]
		elif next == 2 and find_food:
			print "You search the cupboard and there is nothing." 
		elif next == 3:
			print "You open the door to your left" 
			print "---\nYou enter the Garage!\n---\n"
			garage_room()
		elif next == 4 and not key:
			print "You try to open the door to your right, but its Locked!\n" 
		elif next == 4 and key:
			print "You use the key and open the door to your right" 
			print "---\nYou enter the Throne room!\n---\n"
			throne_room()
		elif next == 5:
			print "You open the door behind you"
			print "---\nYou enter the Living room!\n---\n"
			living_room()
		else:
			print "You take a breather."


def garage_room():
	print "It is dark and damp in here."
	print "It's very hard to breathe, and you don't have much air left."
	print "What is your next action"
	print "(1) open door on the right\n(2) open door behind\n(3) search garage\n"

	global game_stats, find_knife, key

	while True:
		next		= int(raw_input("> "))

		if next == 1:
			print "You escape through the door on the right" 
			print "---\nYou enter the Kitchen!\n---\n"
			kitchen_room()
		elif next == 2:
			print "You escape through the door behind" 
			print "---\nYou are back in the LOBBY!\n---\n"
			start()
		elif next == 3 and not key:
			key				= True
			print "You search the Garage and find a key!\n"
		elif next == 3 and key and not find_knife:
			game_stats[2]	+= game_stats[5]
			find_knife	= True
			print "You search again and find the knife!"
		elif next == 3 and key and find_knife:
			dead ("You search one more time and Choke to death!")
		else:
			dead("You do nothing and die of suffocation!")


def living_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you are going insane."
	print "There are 3 doors,  door (1) left, door (2) infront, and door (3) right."
	print "Do you flee for your life through door 1, 2, or 3 \nor 4 you stay and fight?"

	next		= int(raw_input())
	
	if next == 1:
		print "\n---\nYou flee to the Lobby!\n---\n"
		start()
	elif next == 2:
		print "\n---\nYou flee to the Kitchen!\n---\n"
		kitchen_room()
	elif next == 3:
		print "\n---\nYou flee to the Great Hall!\n---\n"
		hall_room()
	elif next == 4:
		print "\nYou lose sanity and eat your head out!!\n"
		dead("Well that was nasty!")
	else:
		living_room()


def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "you are in a dark room."
	print "There are 2 doors,  door (1) infront and door (2) on your right."
	print "Which one do you take, 1 or 2?"
	

	next		= int(raw_input())

	if next == 1:
		print "---\nYou enter the Garage!\n---\n"
		garage_room()
	elif next == 2:
		print "---\nYou enter the Living room!\n---\n"
		living_room()
	else:
		dead("You stumble around the room until you starve.")


print "------\nWelcome to my dumb Game"
print "You enter the Lobby!\n------\n"

start()
