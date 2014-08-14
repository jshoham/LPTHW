# ex48
# ex47\ex47\lexicon.py

direction = ('north', 'south', 'east', 'west',
			'up', 'down', 'left', 'right', 'back')
verb = ('go', 'kill', 'eat')
stop = ('the', 'in', 'of')
noun = ('bear', 'princess')

lexicon = {'direction': direction,
			'verb': verb,
			'stop': stop,
			'noun': noun
			}

def scan(input):
	words = input.split()
	sentence = []
	
	for word in words:
		for type in lexicon:
			if word in lexicon.get(type):
				sentence.append((type, word))
				break
		else:
			num = convert_number(word)
			if num is not None:
				sentence.append(('number', num))
			else:
				sentence.append(('error', word))
	
	return sentence
	
def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None