def oneToThous():
	for i in range (1, 1001):
		if i%2 != 0:
			print i

#oneToThous()

def fiveToThous():
	for i in range (5, 1000000000, 5):
		print i

#fiveToThous()


a = [1, 2, 5, 10, 255, 3]
def sumList(arr):
	snum = 0
	for i in range (0, len(arr)):
		snum += arr[i]


	print snum
	return snum


#sumList(a)

def avgList(arr):
	avg = sumList(arr)/len(arr)
	print avg

avgList(a)