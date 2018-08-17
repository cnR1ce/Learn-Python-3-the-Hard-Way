from sys import argv

script, user_name = argv
propmt = ">"

print(f"Hi,{user_name}, I'm the {script} script.")
print("I'd like to ask you a few question")
print(f"Do you like me {user_name}")
likes = input(propmt)

print(f"Where do you live {user_name})")
lives = input(propmt)

print("What kind of computer do you have?")
computer = input(propmt)

print(f"""
	Alright, so you said {likes} about liking me.
	You live in {lives}. Not sure where that is.
	And you have a {computer} computer. Nice.
	""")

# study drills

#!/usr/bin/env python3

# ex14: Prompting and Passing

from sys import argv

# Add another argument and use it in your script
script, user_name, city = argv
# Change the prompt variable to something else
prompt = 'Please type the answer: '

print("Hi %s from %s, I'm the %s script." % (user_name, city, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("What's the whether like today in %s?" % city)
weather = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
The weather in your city is %s.
But I can't feel it because I'm a robot.
And you have a %r computer.  Nice.
""" % (likes, weather, computer))