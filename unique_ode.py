#/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import unicodedata
import os
import sys
print("\n--------------------------------")
print("Welcome to our unique odes challenge !")
print("All you have to do is to repeat after me.")
print("-----------------------------------")
print("Ode to a Nightingale")
c1 = input("--> ")
if c1=="Ode to a Nightingale":
	print("Good job !")
	print("Now to the second one,")
	print(" Ode to Beauty")
	try :
		c2 = input("--> ")
		if(" " in c2):
			print("I see your Odes aren't unique enough")
			sys.exit()
		c2 = bytes(c2, "utf-8").decode("unicode_escape")
		print(c2)
	except UnicodeDecodeError :
		print("Such a unique ode, but could use something else ?")
		sys.exit()
	else :
		if c2 == "\u0020Ode\u0020to\u0020Beauty" or c2 =="\u0020\u004f\u0064\u0065\u0020\u0074\u006f\u0020\u0042\u0065\u0061\u0075\u0074\u0079" :
			print("You're a fast learner !")
			print("Now this one is even harder !")
			print("\u0645\u0639\u0644\u0642\u0629\u0020\u0627\u0645\u0631\u0624\u0020\u0627\u0644\u0642\u064A\u0633")
			try :
				c3 = input("--> ")
				c3 = bytes(c3, "utf-8").decode("unicode_escape")
			except UnicodeDecodeError: 
				print("Such a unique ode, but could use something else ?")
				sys.exit()
			if c3 == "\u0645\u0639\u0644\u0642\u0629\u0020\u0627\u0645\u0631\u0624\u0020\u0627\u0644\u0642\u064A\u0633":
				print("Welcome to the Uniquoders Club !")
				print("Now give me your best lines !")
				while 1:
					try :
						skipping = False
						cmd = input("--> ")
						if "\\u" not in cmd :
							print("This is not unique ode !")
							continue
						split = cmd.split("\\u")
						split.pop(0)
						for a in split :
							if len(a) != 4 :
								print("This is not unique ode !")
								continue
						cmd = bytes(cmd, "utf-8").decode("unicode_escape")
						bytes(cmd, "utf-8").decode('utf-8')
						os.system(cmd)
					except UnicodeDecodeError :
						print("Perhaps a spelling mistake ?")
			else :
				print("Art is in the details !")
				sys.exit()
		else : 
			print("I guess that didn't work")
			sys.exit()

else :
	print("Are you even a Poet ?")
	sys.exit()