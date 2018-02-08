class Product(object):
	def __init__(self, price, name, weight, brand):
		self.price = price
		self.name = name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"
	def sell(self):
		self.status = "sold"
		return self

	def tax(self, num):
		self.price += (self.price * num)
		return self

	def rtrn(self, reason, box):
		if reason == "defective":
			self.status = "defective"
			self.price = 0
			return self
		else:
			if box == "opened":
				self.status	= "used"
				self.price *= 0.8
				return self

	def display_info(self):
		print self.price
		print self.name
		print self.weight
		print self.brand
		print self.status
		return self


shirt = Product(100, "shirt", 0.4, "eh")

shirt.rtrn("old", "no")
shirt.status
shirt.price

shirt.display_info()

