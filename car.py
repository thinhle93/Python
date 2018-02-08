class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.display_all()

	def display_all(self):
		print "Price", str(self.price)
		print "speed", str(self.speed) + "mph"
		print "Fuel:", str(self.fuel)
		print str(self.mileage) + "mpg"
		tax = 12
		if self.price > 10000:
			tax = 15
		print "tax:", str(tax)


car1 = Car(2000, 35, "full", 105)
car2 = Car(2000, 5, "not full", 95)
car3 = Car(2000, 15, "Kind of Full", 95)
car4 = Car(2000, 25, "Full", 25)
car5 = Car(2000, 45, "Empty", 25)
car6 = Car(2000000, 35, "Empty", 15)