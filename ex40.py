class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	
happy_baby = Song(["Happy","a", "b"])

beat_it = Song(["They told him don't you ever come around here",	
"don't wanna see you face better disappear"])

happy_baby.sing_me_a_song()

beat_it.sing_me_a_song()