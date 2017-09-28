from sys import argv
script, file_name = argv
file = open(file_name)
print file.read(),
file.seek(1)
print file.readline(),
print file.readline(),
