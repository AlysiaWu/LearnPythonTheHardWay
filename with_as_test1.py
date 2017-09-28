try:
	f = open("c:/not_exist.txt")
	try:
		date = f.readline()
	except:
		print "exception!"
	finally:
		print "finally block: close file"
		f.close()
finally:
	print "exception!"

with open("c:/not_exist.txt") as file:
	data = file.read()