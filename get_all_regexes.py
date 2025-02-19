import json

def main():
	with open('uniq-regexes-8.json') as f:
		print('Total Number of lines:', len(f.readlines()))

	with open('uniq-regexes-8.json') as input_file:
		i = 0
		for line in input_file:
			regex = json.loads(line)['pattern']
			with open(f'all_regexes/{i}.txt', 'w') as output_file:
				try:
					print(regex, file=output_file)
				except:
					print('kjhgfcdghjkhgf', file=output_file)
			i += 1

			if i % 1000 == 0:
				print(i)


if __name__ == '__main__':
	main()
