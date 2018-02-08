my_dict = {
	"Speros": "(555) 555-5555",
  	"Michael": "(999) 999-9999",
  	"Jay": "(777) 777-7777"
}

def tup(arg):
	arr = []
	for key,val in arg.iteritems():

		# tup = ()
		tup = (key, arg[key])
		arr.append(tup)

	print arr


tup(my_dict)
