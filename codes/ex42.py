#总结



# Study Drills
#Whatdoes super(Employee, self).__init__(name) do?
# That’s how you can run the __init__method of aparent class reliably.Search for “python3.6super”and read the various advice on it being evil and good for you.








## Animal is-a object( (yes, sort of confusing) look at the extra credit )

class Animal(object):
	pass

## ?
class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__()
		self.name = name

##??
class Cat(Animal):
	def __init__(self, name):
		super(Cat, self).__init__()
		self.name = name

## ??
class Person(object):
	def __init__(self, name):
		##？？
		self.name = name
		##Person has a pet of some kind
		self.pet = None

## ??

class Employee(Person):
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary

##??
class Fish(object):
	pass

##??
class Salmon(Fish):
	pass

##??
class Halibut(Fish):
	pass

## rover is a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

#??
mary = Person("Mary")

##??
mary.pet = santan

##??
frank = Employee("Frank", 120000)

##??
frank.pet = rover

##??
flipper = Fish()

##??
crouse = Salmon()

##??
harry = Halibut()

