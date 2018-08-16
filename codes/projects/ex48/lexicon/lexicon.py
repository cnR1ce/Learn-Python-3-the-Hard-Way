

def scan(sentence):
	"Break up a sentence into words,return a result-list"
	words = sentence.split(' ')
	# analyse words
	result = []
	#for each word, send it to the analyzer to analyze
	for word in words:
		wordtype = analyse(word.lower())
		if word.isdigit():
			word = int(word)
		result.append((wordtype, word))
	return result


def analyse(word):
	'''Analyze word, return the wordtype'''
	rules = {
        "direction": ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
        "verb": ['go', 'stop', 'kill', 'eat'],
        "stop": ['the', 'in', 'of', 'from', 'at', 'it', 'to'],
        "noun": ['door', 'bear', 'princess', 'carbinet']
	}

	if word.isdigit():
		return 'number'

	for rule, rulelist in rules.items():
		if word in rulelist:
			return rule
	return 'error'