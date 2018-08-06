#总结:
#(1)Dictionaries--->Modules--->Classes/Objects 一切都是容器（container）

#(2)访问容器对象的方法：
## dict style--->mystuff['apple']
## module style--->mystuff.apples(), print(mystuff.tangerine)
## class style--->thing = Mystuff(), thing.apple(), print(thing.tangerine)

#(3)OOP(Object-oriented programming)

#(4)study drills

#self属性区分了内部、外部函数和变量，因此要加一个self


#------------------------------------------------

class Song(object):
	"""docstring for Song"""
	def __init__(self, lyrics):
		super(Song, self).__init__()
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)


happy_bday = Song(["Happy birthday to you", "I don't want to get sued","So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family","With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
