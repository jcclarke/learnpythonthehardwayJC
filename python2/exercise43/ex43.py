#!/usr/bin/env python2

from sys import exit
from random import randint
import random

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        print "Engine __init__ has scene_map:", scene_map
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
			print "\n--------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)


class Finish(Scene):

    def enter(self):
        print "Game complete."
        exit(1)


class Death(Scene):

    quips = [
        "You're dead!\nGame Over Yeah!!!!",
        "oh well. I guess your just not good.",
        "Here is some advice.\n:)\nsmile.",
        "Don't be bad. Get Good!"
    ]

    def enter(self):
        print Death.quips[randint(0,len(self.quips) - 1)]
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of planet Percal #25 have invaded your ship and wiped out"
        print "your entire crew. You are the last surviving member and you final"
        print "mission is to get the neutron destructo bomb from the Weapons Armory,"
        print "put it on the bridge, and blow up the ship after getting into an"
        print "Escape Pod"
        print "\n"
        print "You're running down the Central Corridor to the weapons armory when"
        print "A G9thon jumps out infront of you. With red scaley skin, dark grimmy"
        print "hair, wearing a clown suit, and flowing with hate, he stands infront"
        print "of you blocking the door to the Weapons Armory while drawing his gun"
        print "..."
        print "\n"
        print "What will you do?"
        print "shoot"
        print "dodge"
        print "tell a joke\n"

        action = raw_input("> ")

        if action == "shoot":
            print "You are quick on the draw and fire your blaster at the Gothon."
            print "His bright costume distracts you and you miss. The shot leaves"
            print "a cut on his face, and completely shreds his brand new clown"
            print "that his Mom made and give him for his invasion trip. :o"
            print "He goes berserk, lunges at you and shoots repeatedly till you dead!"
            print "He then eats your dead carcus."
            print "eewww!"

            return 'death'

        elif action == "dodge":
            print "The Gothon fires and misses you as you expertly dodge his shot."
            print "He fires repeatedly and you spin dodge each shot getting closer"
            print "and closer to the Gothon after each dodge. Finally the Gothon"
            print "runs out of ammo and you run straightat him. You fall face first"
            print "infront of the Gothon from the dizzyness of all the spinning."
            print "You immediately roll, only to see a giant colourful foot."
            print "He crushes your head, and proceedes to eat your hands and feet!"

            return 'death'

        elif action == "tell a joke":
            print "Luckily, you remember from your training acadamy that most Gothons"
            print "love a good joke. You remember a joke that your roommate was who"
            print "was learning Gothonic told you and yiu tell it to the gothon."
            print "sjfjf duhs wirhf sidhge sigi t uoh dijtbf ducur rustfw dhhdddd!"
            print "The Gothon pauses trying hard not to laugh but gives in and bursts"
            print "out in laughter. Seizing the opportunity, you run up to him and"
            print "shoot him in the head. You jump over his dead body and kick the"
            print "door open and enter the Weapons Armory"
            return 'laser_weapon_armory'

        else:
            print "DID NOT COMPUTE!"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "you pie into the weapons armory and then dive roll behind the a"
        print "weapons stash. You scan the room floor more Gothons that might be"
        print "hiding. It is eerily quiet, but you see the neutron bomb in the"
        print "far corner of the room in its box. You stand up and make a dash"
        print "to the box. You get to the box and see a 3 digit key pad lock on"
        print "the box. You have 10 tries to guess the code. After try 20, it is"
        print "locked forever\n"
        print "You can either enter a code or search box for a clue"
        print "what will you do?"
        print "type 'search' or enter 3 digits\n"


        code = "%d%d%d" % (randint(1,3), randint(1,3), randint(1,3))
        action = raw_input("> ")
        guess = action
        guesses = 0

        while guesses < 20:
            if action == "search":
                print "You search the box and see some marker writing on the side."
                print "It says 'each digit is between 1 and 3"
                print "\ntype 'search' or enter 3 digits\n"

                action = raw_input("> ")
                guess = action

            elif (guess == code) or (guess == "444"):
        	    print "The box clicks and you see white gas stream out as it slowly opens."
        	    print "You grab the bomb and run quickly to the door to the bridge where,"
        	    print "you must place it."
        	    return 'the_bridge'

            else:
                print "You typed on the keypad"
                print "[keypad]>%s" % guess
                print "BBBZZZZDDDDD!"
                guesses += 1

                print "'search' or enter 3 digits\n"

                action = raw_input("> ")
                guess = action

        print "The box buzzes one last time, and you turn sick to your stomach as"
        print "hear the sound you only heard during training at the academy."
        print "Then you remember the code was %s" % code
        print "THE BOX IS FUSING SHUT FOREVER."
        print "You sit on the ground stunned awaiting death!"
        print "The Gothon ship fires at your ship. You die in the explosion!"
        
        return 'death'



class TheBridge(Scene):

    def enter(self):
        print "You make your way through the halls of the ship towards the"
        print "bridge. You open the door and see 6 Gothons all dressed in"
        print "clown suits, each uglier than the next. They turn and look"
        print "at you and they see the neutron bomb in your arm. They haven't"
        print "pulled out their blasters yet."
        print "What do you do?\n"
        print "throw the bomb"
        print "place bomb carefully"

        action = raw_input("> ")


        if action == "throw the bomb":
            print "In a panic, you throw the bomb at the group of Gothons and"
            print "make a leap for the door. Before you get through the door, a"
            print "Gothon manages to blast off your left leg. You make it though"
            print "the door and manage to lock it behind you, but you slowly lose" 
            print "conciousness from rapid blood loss. You died"
            print "While dying, you hear the Gothons screem trying to disarm the"
            print "bomb. You smile as you know soon they will be blown to bits!"

            return 'death'

        elif action == "place bomb carefully":
            print "You point your blaster at the bomb and shout in Gothonic"
            print "\"gfyfhg hfbfb, owprb hduuwi wjsd!\"\n"
            print "Anyone move, we all dead!"
            print "You slowly place the bomb down in front of you while staring"
            print "down those clowns with the blaster aimed at the bomb. You walk"
            print "backwards and open the door behind you all the while never"
            print "shifting your stare or aim. You close the door on them and"
            print "blast the lock sealing them in. You then make your escape."

            return 'escape_pod'

        else:
            print "DID NOT COMPUTE!"
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print "You run frantically around the ship, and there are hardly any"
        print "Gothons around. The coast is clear so pass the mess hall and"
        print "the kitchen, go through the change room, and into the emergency"
        print "chambers where the escape pods are located."
        print "There are 5 escape pods in the room and some of them might be"
        print "damaged. Not having time to inspect them, you jump into one"
        print "and pull the release switch."
        print "Which one did you choose?\n"

		# 3 out of 5 pods are good
        good_pods = random.sample(range(1,5), 3)

        try:
            guess = int(raw_input("POD-> "))
        except ValueError:
            print "DID NOT COMPUTE!"
            return 'escape_pod'

        if guess in good_pods:
            print "Soon after getting into pod %s, it launches smoothly into" % guess
            print "space towards the nearby planet below. As you you get close"
            print "to the planet, you look back at your ship as it implodes and"
            print "explodes which creates a bright light, joining all the other"
            print "lights from the stars in space. The ship and the Gothons in"
            print "it have all disintegrated\n"
            print "YOU WON!"

            return 'finish'

        elif (guess not in good_pods) and (guess in range(1,5)):
            print "Soon after getting into pod %s, it launches into the void" % guess
            print "of space. Sunddenly the pod starts to violently shake, as"
            print "the hole that was in its get wider. The pod implodes, and"
            print "crushes you into a thick paste. You died!!"

            return 'death'

        else:
            print "Excape pod %s is not available." % guess
            return 'escape_pod'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finish': Finish()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)



a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
