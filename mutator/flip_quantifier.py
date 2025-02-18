import random

from my_regex_constants import *

def flip_quantifier(data):
	"""
	Look for quantifiers (*, +, ?) in the data; pick one and flip it 
	to another quantifier or remove it.
	"""
	positions = [i for i, c in enumerate(data) if c in REGEX_QUANTIFIERS]
	if not positions:
		return data
		# return insert_known_token(data)

	pos = random.choice(positions)
	old_q = data[pos]
	
	if random.random() < 0.3:
		new_data = data[:pos] + data[pos+1:]
		return new_data
	
	new_q = random.choice(REGEX_QUANTIFIERS)
	while new_q == old_q:
		new_q = random.choice(REGEX_QUANTIFIERS)
	data[pos] = new_q

	return data
