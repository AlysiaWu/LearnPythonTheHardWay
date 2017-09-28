people = 30
cars = 30
buses = 15

if cars >= people:
	print "cars >= ppl"
elif cars < people:
  print "cars < people"
elif cars == people:
  print "cars == people"
else:
 print "cars = people"

if buses > cars:
	print "Too many buses."
elif buses < cars:
	print "Too many cars."
else:
	print "car equal bus"

if people > buses:
	print "people > buses"
else:
	print "people = buses"