import random

def coinToss():
	print "Starting the program..."
	heads = 0
	tails = 0
	for i in range (1,101):

		x = round(random.random())

		if x == 0:
			heads += 1
			result = "head"
		elif x == 1:
			tails += 1
			result = "tail"

		print "Attempt #" + str(i) + " : Throwing a coin... It's a " + result + "! ... Got "+ str(heads) + "head(s) so far and " + str(tails) +"tail(s) so far"
		print "Ending the program, thank you!"

coinToss()