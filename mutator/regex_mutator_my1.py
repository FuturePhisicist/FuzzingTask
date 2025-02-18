#!/usr/bin/env python
# encoding: utf-8
"""
A Python custom mutator for AFL++ that performs simple grammar-like mutations on
regex strings.

Adapted from a simpler example by Christian Holler (:decoder)
https://github.com/AFLplusplus/AFLplusplus/blob/stable/custom_mutators/examples/example.py.
"""

import random

from insert_known_token import insert_known_token
from handle_bracket_expression import handle_bracket_expression
from flip_quantifier import flip_quantifier
from random_deletion import random_deletion
from invalidate_regex import invalidate_regex

from my_regex_constants import *

def init(seed):
	random.seed(seed)

def fuzz(buf, add_buf, max_size):
	# If the input buffer is empty, provide a minimal regex
	if not buf:
		buf = SAMPLE_REGEX.encode("utf-8", errors="ignore")

	try:
		text = buf.decode("utf-8", errors="ignore")
	except:
		text = SAMPLE_REGEX

	data = list(text)

	num_mutations = random.randint(1, MAX_MUTATIONS_CNT)
	for _ in range(num_mutations):
		data = mutate_regex_dispatcher(data)

	mutated_str = "".join(data)
	mutated_bytes = mutated_str.encode("utf-8")

	# Enforce max_size by truncating if too big
	if len(mutated_bytes) > max_size:
		mutated_bytes = mutated_bytes[:max_size]

	return bytearray(mutated_bytes)


# Main "dispatcher" function
def mutate_regex_dispatcher(data):
	mutations = [
		insert_known_token,
		handle_bracket_expression,
		flip_quantifier,
		random_deletion,
		invalidate_regex
	]
	mutation_func = random.choice(mutations)
	return mutation_func(data)
