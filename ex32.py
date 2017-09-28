the_count = [1,2,3,4,5]
fruits = ['apple',"banana",'orange']
change = [1, "pennies", 2, 'dimes', 3, 'quarters']

# the 1st kind of for-loop go through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also can go through mixed list.
# note we have to use %r as we don't know what's in it.
for i in change:
	print "I got %r" % i

# we can also build a list. first starts with an empty one.
elements = []

# then use the range function to do 0 to 5 counts.
for i in range (0, 6, 2):
	print "Adding %d to the lise." %i
	# append is a function that list understand
	elements.append(i)

for i in elements:
	print "Element was: %d" % i

elements2 = range(0, 20, 5)
for i in elements2:
	print "Element2 was: %d" % i