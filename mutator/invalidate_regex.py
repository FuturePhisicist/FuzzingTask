import random

from my_regex_constants import *

def invalidate_regex(data):
	# Convert to a list so we can insert/delete in place
	data = data[:]

	num_mutations = random.randint(1, MAX_INVALIDATIONS_CNT)
	for _ in range(num_mutations):
		data = invalidate_regex_dispatcher(data)

	return data

# Invalidate "dispatcher" function
def invalidate_regex_dispatcher(data):
	mutations = [
		insert_random_regex_specials,
		replace_random_regex_special
	]
	mutation_func = random.choice(mutations)
	return mutation_func(data)

def insert_random_regex_specials(data):
	how_many = random.randint(1, MAX_INSERT_CHAR_CNT)
	specials_seq = [random.choice(REGEX_SPECIALS) for _ in range(how_many)]
	pos = random.randint(0, len(data))
	data = data[:pos] + specials_seq + data[pos:]

	return data

def replace_random_regex_special(data):
	# Find all positions of existing specials in data
	special_positions = [i for i, ch in enumerate(data) if ch in REGEX_SPECIALS]
	if special_positions:
		pos = random.choice(special_positions)
		old = data[pos]
		new = random.choice(REGEX_SPECIALS)
		while new == old:
			new = random.choice(REGEX_SPECIALS)
		data[pos] = new

	return data
