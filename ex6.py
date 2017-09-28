x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s. " %(binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: %s." % x

hilarious = False
joke_evaluation = "Isn't that joke funny?! % r % s"

temp = joke_evaluation % (hilarious,'wahaha! ')

w = "This is the left side of..." 
e = "a string with right side."

z = 10

print w + e , z

print  temp + y