from sys import argv

script, filename = argv

print "We'll erase %r." % filename
print "If you don't wanna do that, press CTRL-C (^C)."
print "If you wanna do that, press RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncation the file. Goodbye!"
target.truncate()

print "Now I'll ask you for 3 lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 1: ")

print "I'll write these to file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Finally, we close it"
target.close()