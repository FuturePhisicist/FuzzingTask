import random

from my_regex_constants import *

def insert_known_token(data):
	pos = random.randint(0, len(data))
	token = random.choice(REGEX_SPECIALS)

	if token == "[":
		bracket_text = "[" + random_bracket_content() + "]"
		new_data = data[:pos] + list(bracket_text) + data[pos:]
	elif token == "{":
		bracket_text = "{" + random_curly_bracket_content() + "}"
		new_data = data[:pos] + list(bracket_text) + data[pos:]
	elif token == "(":
		pos1 = random.randint(0, len(data))
		pos2 = random.randint(0, len(data))
		pos1, pos2 = min(pos1, pos2), max(pos1, pos2)

		# pos1 == pos2 will create empty parentheses -> no problem
		new_data = data[:pos1] + ["("] + data[pos1:pos2] + [")"] + data[pos2:]
	else:
		new_data = data[:pos] + [token] + data[pos:]

	return new_data


def random_bracket_content():
	segments_cnt = random.randint(1, MAX_SEGMENTS_CNT)
	bracket_chars = []

	if random.random() < 0.2:
		bracket_chars.append("^")

	for _ in range(segments_cnt):
		c1 = random.choice(BRACKET_INNERS)
		c2 = random.choice(BRACKET_INNERS)
		if random.random() < 0.5:
			if c1 > c2:
				c1, c2 = c2, c1
			bracket_chars.append(f"{c1}-{c2}")
		else:
			bracket_chars.append(c1)

	return "".join(bracket_chars)

def random_curly_bracket_content():
	m = random.randint(0, MAX_OCCURANCE_CNT)
	data = str(m)

	if random.random() < 0.5:
		data += ','
		if random.random() < 0.5:
			n = random.randint(0, MAX_OCCURANCE_CNT)
			data += str(n)

	return data
