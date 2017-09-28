class Animal(object):
	def call(self):
		pass

class Dog(Animal):
	def __init__(self, name):
		self.name = name
	
	def call(self):
		print self.name, 'Wang wang!'
		
class Cat(Animal):
	def __init__(self, name):
		self.name = name
	
	def call(self):
		print self.name, 'Miao miao!'
		
class Person(object):
	def __init__(self, name):
		self.name = name
		self.pet = None
	
	def speak(self):
		if(self.pet != None):
			print 'My name is', self.name, ',I have a pet named', self.pet.name
		else:
			print 'My name is', self.name, ',I have no pet'

class Employee(Person):
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary
	
	def speak(self):
		super(Employee, self).speak()
		print 'And my salary is %s' % self.salary
	
kala = Dog("Kala")
mimi = Cat("Mimi")

kala.call()
mimi.call()

mary = Person("Mary")
mary.pet = mimi
mary.speak()

tom = Employee("Tom", 120000)
tom.speak()

