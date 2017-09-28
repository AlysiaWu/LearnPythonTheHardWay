print "You enter a dark room with 2 doors. Do you want to open door 1 or door 2?"

door = raw_input("> ")

if door == "1":
	print "there is a gaint bear here eating cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

else:
	print "You stumble around and fall on a knife and die. Good job!"
		
	
	
	
	
#just practice.
x = 10
print (1 < x < 10)
print (10 > x > 1)
print (x > 1 and x < 10)
print (x in range(1, 10) )
	
	
	
	
	
	
	
	