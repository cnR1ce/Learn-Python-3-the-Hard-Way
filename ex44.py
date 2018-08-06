#Inheritance vesus Composition

#summary:

#When you are doing this kind of specialization, there are three ways that the parent and child classes can interact:
# 1. Actions on the child imply an action on the parent.
# 2. Actions on the child override the action on the parent.
# 3. Actions on the child alter the action on the parent.

#
#If both solutions solve the problem of reuse, then which one is appropriate in which situations? The answer is incredibly subjective, but I’ll give you my three guidelines for when to do which:
# 1. Avoid multiple inheritance at all costs, as it’s too complex to be reliable. If you’re stuck with it, then be prepared to know the class hierarchy and spend time ﬁnding where everything is coming from.
# 2. Use composition to package code into modulesthatareusedinmanydifferentunrelatedplaces and situations.
# 3. Use inheritance only when there are clearly related reusable pieces of code that ﬁt under a single common concept or if you have to because of something you’re using.

#
#






# ex44a.py implicit inheritance

class Parent(object):
	"""docstring for Parent"""
	def implicit():
		print("PARENT implicit():")

class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# ex44b.py Override Explicitly

class Parent(object):
	"""docstring for Parent"""

	def override(self):
		print("PARENT override()")

class Child(Parent):

	def override(slef):
		print("CHILD override")

dad = Parent()
son = Child()

dad.override()
son.override()


# ex44c.py Aleter Before of After

class Parent(object):
	"""docstring for Parent"""

	def altered(self):
		print("PARENT altered()")

class Child(Parent):

	def altered(slef):
		print("CHILD, BEFORE PARENT altered()")
		super(Child, self).altered()
		print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()


class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

