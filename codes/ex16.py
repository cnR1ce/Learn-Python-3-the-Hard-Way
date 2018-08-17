from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target=open(filename,"w")

print("Truncating the file, Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("I'm going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it")
target.close()

#study drills

#!/usr/bin/env python3

# ex16: Reading and Writing Files

from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# Open this file in 'write' mode
target = open(filename, 'w')

print("Truncating the file.  Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print("And finally, we close it.")
target.close()


#!/usr/bin/env python3

# A script similar to ex16 that uses read and argv to read the file

from sys import argv

script, filename = argv

print("The contents of the file %s:" % filename)
target = open(filename)
contents = target.read()
print(contents)
target.close()