class bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
		print self.price, self.max_speed, self.miles
		return self
	def ride(self):
		print "Riding"
		self.miles += 10
		return self
	def reverse(self):
		print "Reversing"
		self.miles -= 5
		return self
b1 = bike(100,150)
b2 = bike(200,170)
b3 = bike(400, 210)


b1.ride().ride().ride().reverse().displayInfo()
b2.ride().ride().reverse().reverse().displayInfo()
b3.reverse().reverse().reverse().displayInfo()