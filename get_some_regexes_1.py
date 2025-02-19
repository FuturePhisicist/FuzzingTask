import random
import json

def main():
	with open('uniq-regexes-8.json') as input_file:
		random_lines = random.sample(input_file.readlines(), 1000)
	for i, line in enumerate(random_lines):
		regex = json.loads(line)['pattern']
		with open(f'some_regexes/{i}.txt', 'w') as output_file:
			try:
				print(regex, file=output_file)
			except:
				print('kjhgfcdghjkhgf', file=output_file)
		i += 1

		if i % 1000 == 0:
			print(i)


if __name__ == '__main__':
	main()
