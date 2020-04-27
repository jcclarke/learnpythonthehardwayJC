#!/usr/bin/env python3

import mystuff

# First we have a mystuff dictionary
mystuff_40	= {'apple': "I AM APPLES!"}
	#get apple from dictionary
print (mystuff_40['apple'] )

	# get apple and variable from module
mystuff.apple()
print (mystuff.tangerine)

	# get apple and variable from class
thing		= mystuff.mystuff_class()	# used with <import mystuff>
# thing		= mystuff_class()			# used with <from mystuff import *>
print (thing.tangerine)
thing.apple_func()


class Song (object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print (line)

happy_bday			= Song(["Happy borthday to you",
							"I don't want to get sued",
							"So I'll stop right there"])

bulls_on_parade		= Song(["They rally around the family",
							"With pockets full of shells"])


happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
