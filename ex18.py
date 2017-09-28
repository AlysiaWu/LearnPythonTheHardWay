# this one is like your script with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this.
def print_two_again(args1, args2):
	print "arg1: %r, arg2: %r" % (args1, args2)

# this just takes one argument
def print_one(a):
	print "arg1: %r" % a

# this takes no argument
def print_none():
	print "I got nothing'."

print_two("Z","S")
print_two_again("Z","S")
print_one('s')
print_none()