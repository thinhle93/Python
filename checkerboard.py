def checkerboard():
	for i in range (1, 9):
		if i%2 != 0:
			star = ""
			for x in range (1, 9):
				if x%2 != 0:
					star += "*"
				else:
					star += " "
		elif i%2 == 0:
			star = ""
			for j in range (1, 9):
				if j%2 == 0:
					star += "*"
				else:
					star += " "
		print star

checkerboard()


