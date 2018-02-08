students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def pnames(x):
	for i in range (0, len(x)):
		name = ""
		for val in x[i].itervalues():
			name += val + " "
		print name

# pnames(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def pnames2(x):
	for key, data in x.items():
		count = 0
		for value in data:
			count += 1
			print str(count), "-",value["first_name"], value["last_name"], "-", str(len(value["first_name"]) + len(value["last_name"]))


	# for key in x.iterkeys():
	# 	for i in range(0, len(key)):
	# 		print x[key][i]
	
	# for key, data in x.items():
	# 	count = 0
 #     #print data
    	
	#     for value in data:
	#     	count += 1
	# 	    print count value["first_name"], value["last_name"]
		        



pnames2(users)

# print users['Students'][0]