#input
l = ['magical unicorns',19,'hello',98.98,'world']
o = [2,3,1,7,4,12]
m = ['magical','unicorns']

def listType(arr):
	count = 0
	data = type(arr[0])
	data2 = ""

	string = "String:"
	Sum = 0

	for i in range(0, len(arr)):

		if type(arr[i]) != data:
			count += 1

			

		if type(arr[i]) == str:
			string += " " + arr[i]
		elif type(arr[i]) == int:
			Sum += arr[i]
				
		elif type(arr[i]) == float:
			Sum += arr[i]
				

		


	if count > 0:
		data2 = "mixed"

	if data2 != "mixed":
		if data == str:
			data2 = "string"

		elif data == int:
			data2 = "integer"
		elif data == float:
			data2 = "float"
		elif data == bool:
			data2 = "boolean"

	print "The list you entered is of " + data2 + " type"
	if data2 == "string":
		print string
	elif data2 == "integer" or data2 == "float":
		print "Sum: " + str(Sum)
	elif data2 == "mixed":
		print string 
		print "Sum: " + str(Sum)


listType(m)


