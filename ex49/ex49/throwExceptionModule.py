class ZxwException(Exception):
	pass

class Ex49Class:
	def testException(self, number):
		if(number == 0):
			return 'pass'
		else:
			raise ZxwException('ZxwException occurred!')

#ex49C = Ex49Class()
#result = ex49C.testException(0)