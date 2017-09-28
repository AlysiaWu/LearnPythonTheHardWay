from b import B

class A(object):
	def __init__(self, b):
		self.b = b
		
	def f(self):
		self.b.f()
b = B()		
a = A(b)
a.f()