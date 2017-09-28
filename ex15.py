from sys import argv

script, filename = argv

txt = open(filename)

print "Here is your file: ", filename
print txt.read()
txt.close()

file_again = raw_input("Type the filename again:\r\n> ")
txt_again = open(file_again)

print txt_again.read()
txt_again.close()