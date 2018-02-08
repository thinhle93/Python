def findReplace(string):
	print string.find("day")
	return string.replace("day", "month")


mystr = "It's Thanksgiving day. It's my birthday, too!"

findReplace(mystr)


x = [2, 54, -2, 7, 12, 98]
def min_max(arr):
	print min(arr)
	print max(arr)

min_max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
def fnl(arr):
	print arr[0]
	print arr[-1]

	newarr = []
	newarr.append(arr[0])
	newarr.append(arr[-1])
	print newarr

fnl(x)


x = [19,2,54,-2,7,12,98,32,10,-3,6]
def newlist(arr):
	first = sorted(arr)

	newarr = []
	newarr.append(first[:5])
	for x in range(5, len(first)):
		newarr.append(first[x])

	print newarr

newlist(x)