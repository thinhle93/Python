x = x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def printStars(arr):
	for i in range (0, len(arr)):
		temp =""

		if type(arr[i]) == str:
			result = arr[i][0]
			for x in range (0, len(arr[i])):
				temp += result.lower()
		else:
			result = "*"

			for x in range (0, arr[i]):
				temp += result
		print temp


printStars(x)