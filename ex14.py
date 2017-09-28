from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the s% script." %(user_name, script)
print "I'd like to ask you some questions."
print "%s, do you like me?" % user_name
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print"""
Well, so you said %r about like me.
You live in %r. Not sure where that it.
And you have a %r computer. Nice.
"""%(likes, lives, computer)
