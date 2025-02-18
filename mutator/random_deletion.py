import random

from my_regex_constants import *

def random_deletion(data):
	if len(data) < 2:
		return data

	start = random.randint(0, len(data) - 1)
	length = random.randint(1, min(MAX_REMOVE_CHAR_CNT, len(data) - start))
	new_data = data[:start] + data[start+length:]
	return new_data
