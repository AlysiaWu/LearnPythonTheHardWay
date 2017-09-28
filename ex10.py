fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print fat_cat

s1 = "It's \"Sparta!\""
s2 = 'It\'s "Sparta!"';
print "He said: %s %s" % (s1, s2)
print "He said: %r %r" % (s1, s2)

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,

