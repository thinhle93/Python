def say():

	for i in range (2, 10):
		state = ""
		for x in range(2, i):
			if i%x == 0:
				state = str(i) + "not prime"
				break
			state = str(i) + "prime"
		print state

		

say()