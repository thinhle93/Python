def oddEven():
	for i in range(1, 2001):
		if i%2 == 0:
			check = "even"
		else:
			check = "odd"

		print "Number is " + str(i) + ". This is an " + check + " number."

#oddEven()

def multiply(arg, num):
	for i in range (0, len(arg)):
		arg[i] = arg[i] * num
	return arg


a = [2,4,10,16]
# b = multiply(a, 5)
# print b


def layered_multiples(arr):
	newarr = []
	for i in range (0, len(arr)):
		temp = []
		for x in range (0, arr[i]):
			temp += "1"
		newarr.append(temp)

	return newarr



# x = layered_multiples(multiply([2,4,5],3)) #[6,12,15]
# print x


