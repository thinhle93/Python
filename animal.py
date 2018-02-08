class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def display_health(self):
		print self.health
		return self



class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name, 150)
	def pet(self):
		self.health += 5

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name, 170)
	def fly(self):
		self.health -= 10
		return self
	def display(self):
		self.display_health()
		print "I am a Dragon"
		return self

# dog1 = Dog("spot")
# dog1.walk().run()
# print dog1.name
# print dog1.health

an1 =  Animal("one", 90)
an1.display()
d1 = Dragon("whatever")

