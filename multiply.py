def chart():
	print "x 1 2 3 4 5 6 7 8 9 10 11 12"
	for x in range (1, 13):

		line = str(x)
		# if x == 0:
		# 	line += " " + str(x)
		# if x > 0:
		for i in range (1, 13):
			line += " " + str(i * x)

		print line



chart()