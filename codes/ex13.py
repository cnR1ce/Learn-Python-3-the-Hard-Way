#!/usr/bin/env python3

# ex13: Parameters, Unpacking, Variables

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

#study drills 1

# ex13: Parameters, Unpacking, Variables
# Write a script that has fewer arguments

from sys import argv

script, first_name, last_name = argv

print("The script is called:", script)
print("Your first name is:", first_name)
print("Your last name is:", last_name)

#study drill 2
#!/usr/bin/env python3

# ex13: Parameters, Unpacking, Variables
# Write a script that has more arguments.

from sys import argv

script, name, age, height, weight = argv

print("The script is called:", script)
print("Your name is:", name)
print("Your age is:", age)
print("Your height is %d inches" % int(height))
print("Your weight is %d pounds" % int(weight))

#study drill 3
#!/usr/bin/env python3

# ex13: Parameters, Unpacking, Variables
# Combine input with argv to make a script that gets more input from a user.

from sys import argv

script, first_name, last_name = argv

middle_name = input("What's your middle name?")

print("Your full name is %s %s %s." % (first_name, middle_name, last_name))