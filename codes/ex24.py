print("Let's practice everything.")
print('You\'d need to know \'about escapes with \\ that do :')
print('\n new lines and \t tabs.')

poem="""
\t The lovely world
with logic so firmly planted
can not discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print('-------------')
print(poem)
print('-------------')

five = 10-2+3-6
print(f'This should be five:{five}')

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans/1000
	crates = jars /100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

#remember that this is another way to format a string
print("With a starting point of : {0}".format(start_point))
#it is just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point=start_point / 10
print("We can also do that this way:")
formula = secret_formula(start_point)

print("We'd have {}beans, {} jars, and {} crates.".format(*formula))
