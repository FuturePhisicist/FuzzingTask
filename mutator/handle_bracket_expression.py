import random

from my_regex_constants import *

def handle_bracket_expression(data):
	bracket_pairs = find_bracket_pairs(data)
	if not bracket_pairs:
		return data
		# return insert_known_token(data)

	start, end = random.choice(bracket_pairs)
	inside = data[start+1:end]

	inside = mutate_bracket_content(inside)

	new_data = data[:start+1] + inside + data[end:]

	return new_data


def find_bracket_pairs(data):
	stack = []
	pairs = []
	for i, ch in enumerate(data):
		if ch == "[":
			stack.append(i)
		elif ch == "]" and stack:
			start = stack.pop()
			pairs.append((start, i))

	return pairs


def mutate_bracket_content(inside):
	"""
	Tweak the content inside a bracket expression:
	- Insert '^' at the start (negation)
	- Flip random characters
	- ! Insert random range	# not implemented, because the whole expressions can be added
	"""
	# Convert to list for easier changes
	chars = inside[:]

	if (not chars or chars[0] != "^") and (random.random() < 0.2):
		chars.insert(0, "^")

	# Flip a random character
	if chars:
		pos = random.randint(0, len(chars)-1)
		old_char = chars[pos]
		new_char = random.choice(BRACKET_INNERS)
		# just ensure difference
		while new_char == old_char:
			new_char = random.choice(BRACKET_INNERS)
		chars[pos] = new_char

	return chars
