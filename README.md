### ![](/assets/LPTHW1.png)

### Learn Python The Hard Way![](/assets/python3.png)

---

[![Travis](https://img.shields.io/badge/Python-中文版-brightgreen.svg)](https://www.2cto.com/shouce/Pythonbbf/index.html)  [![](/assets/LPTHW0.png)](https://learnpythonthehardway.org/book/)

* Preface
* Introduction: The Hard Way Is Easier
* Exercise 0: The Setup
* Exercise 1: A Good First Program
* Exercise 2: Comments And Pound Characters
* Exercise 3: Numbers And Math
* Exercise 4: Variables And Names
* Exercise 5: More Variables And Printing
* Exercise 6: Strings And Text
* Exercise 7: More Printing
* Exercise 8: Printing, Printing
* Exercise 9: Printing, Printing, Printing
* Exercise 10: What Was That?
* Exercise 11: Asking Questions
* Exercise 12: Prompting Peopley
* Exercise 13: Parameters, Unpacking, Variables
* Exercise 14: Prompting And Passing
* Exercise 15: Reading Files
* Exercise 16: Reading And Writing Files
* Exercise 17: More Files
* Exercise 18: Names, Variables, Code, Functions
* Exercise 19: Functions And Variables
* Exercise 20: Functions And Files
* Exercise 21: Functions Can Return Something
* Exercise 22: What Do You Know So Far?
* Exercise 23: Read Some Code
* Exercise 24: More Practice
* Exercise 25: Even More Practice
* Exercise 26: Congratulations, Take A Test!
* Exercise 27: Memorizing Logic
* Exercise 28: Boolean Practice
* Exercise 29: What If
* Exercise 30: Else And If
* Exercise 31: Making Decisions
* Exercise 32: Loops And Lists
* Exercise 33: While Loops
* Exercise 34: Accessing Elements Of Lists
* Exercise 35: Branches and Functions
* Exercise 36: Designing and Debugging
* Exercise 37: Symbol Review
* Exercise 38: Doing Things To Lists
* Exercise 39: Dictionaries, Oh Lovely Dictionaries
* Exercise 40: Modules, Classes, And Objects
* Exercise 41: Learning To Speak Object Oriented
* Exercise 42: Is-A, Has-A, Objects, and Classes
* Exercise 43: Gothons From Planet Percal \#25
* Exercise 44: Inheritance Vs. Composition
* Exercise 45: You Make A Game
* Exercise 46: A Project Skeleton
* Exercise 47: Automated Testing
* Exercise 48: Advanced User Input
* Exercise 49: Making Sentences
* Exercise 50: Your First Website
* Exercise 51: Getting Input From A Browser
* Exercise 52: The Start Of Your Web Game
* Advice From An Old Programmer
* Next Steps
* Appendix A: Command Line Crash Course

##### Preface

> My book gives you your"programming black belt".

##### Introduction: The Hard Way Is Easier

> Three most essential skills that a beginning programmer needs to know: **reading and writing, attention to detail, and spotting differences.**

##### Exercise 0: The Setup

> Get your computer to run Python

##### Exercise 1: A Good First Program

```py
print("Hello World!")
print ("Hello Again")
print ("I like typing this.")
print ("This is fun.")
print ('Yay! Printing.')
print ("I'd much rather you 'not'.")
print ('I "said" do not touch this.')
```

> **Note**
>
> An "**octothorpe**" is also called a **"pound", "hash", "mesh",** or any number of names. Pick the one that makes you chill out.
>
> **Warning**
>
> If you are from another country, and you get errors about ASCII encodings, then put this at the top of your Python scripts:
>
> ```py
> # -*- coding: utf-8 -*-
> ```
>
> It will fix them so that you can use Unicode UTF-8 in your scripts without a problem.

##### Exercise 2: Comments and Pound Characters

```py
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

print("I could have code like this.") # and the comment after is ignored

# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."

print("This will run.")
```

##### Exercise 3: Numbers and Math

Names:

* +plus
* -minus
* /slash
* \*asterisk
* %percent
* &lt;less-than
* &gt;greater-than
* &lt;=less-than-equal
* &gt;=greater-than-equal

```py
print("I will now count my chickens:")

print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)

print( "What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
```

##### Exercise 4: Variables And Names

```py
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")
```

> **Note**
>
> The\_inspace\_in\_a\_caris called anunderscore character. Find out how to type it if you do not already know. We use this character a lot to put an imaginary space between words in variable names.

##### Exercise 5: More Variables and Printing

```py
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print ("Let's talk about %s." % my_name)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))
```

##### Exercise 6: Strings And Text

```py
types_of_people = 10
x = f"There are {types_of_people} types of people"

binary = 'binary'
do_not = "don't"
y=f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I sid: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?!{}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side"

print(w + e)
```

##### Exercise 7: More Printing

```py
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # what'd that do?
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# watch end = ' ' at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12, end='')
print(end1)
```

##### Exercise 8:Printing,Printing

```py
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("Try your","Own text here","Maybe a poem","Or a song about fear"))
```

##### Exercise 9:Printing,Printing,Printing

```python
# Here's some new strange stuff, remember type it exactly
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print("Here are the days: ", days)
print("Here are the months: ", months)
print("""There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6. 14
""")
```

##### Exercise 10: What Was That?

```python
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print("\a"+"\n"+"\b"+"\n"+"\f"+"\n"+"\r"+"\n"+"\t"+"\n"+"\v")
```

##### Exercise 11: Asking Questions

```python
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
```

##### Exercise 12: Prompting  People

```python
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
```

##### Exercise 13: Parameters, Unpacking, Variables

```python
from sys import argv
# read the WYSS section for how to run this

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is：", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
```



