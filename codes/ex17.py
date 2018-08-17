from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exists? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, "w")
out_file.write(indata)

print("Alright, all down")

out_file.close()
in_file.close()


#study drills

#!/usr/bin/env python3

# ex17: More Files

from sys import argv

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())
