i = 0
numbers = []

while i < 6:
	print(f"At the top i is {i}")
	numbers.append(i)

	i = i + 1
	print("numbers now:",numbers)
	print(f"At the bottom i is {i}")

print("The numbers:")

for num in numbers:
	print(num)


# study drills
#!/usr/bin/env python3

# ex33: While Loops

def createNumbers(max, step):
    i = 0
    numbers = []
    for i in range(0, max, step):
        print("At the top i is %d" % i)
        numbers.append(i)

        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)
    return numbers

numbers = createNumbers(10, 2)

print("The number: ")

for num in numbers:
    print(num)