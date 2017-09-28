def addNum(max, step):
	i = 0
	numbers = []
	while(i < max):
		print "At the top i is %d" % i
		numbers.append(i)
		i += step
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	return numbers

numbers = addNum(10, 2)
print "The numbers: ", numbers
for num in numbers:
	print num
	
# below is add point item.
numbers = []
print "######## Now use for-loop instead of while-loop##########"
def addNum_for(max, step):
	numbers = []
	for i in range(0, max, step):
		numbers.append(i)
	return numbers
numbers = addNum_for(10, 2)
print "The numbers: ", numbers