lyrics = ['hello','world']

class Song(object):
	def __init__(self):
		self.a = lyrics
		b = lyrics
	
	def sing(self):
		for line in self.a:
			print line

songA = Song()
songA.sing()
songA.a = ['b','c']
songA.sing()