name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
	new_dict = zip(list1,list2)
  	# your code here
  	# for i in range (0, len(list1)):
  	# 	new_dict[list1[i]] = list2[i]

  	print dict(new_dict)
  	return new_dict

make_dict(name, favorite_animal)