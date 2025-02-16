import json
import random

def main():
	with open('uniq-regexes-8.json') as f:
		lines = f.readlines()

	data = json.loads(lines[3])
	print(data['pattern'])

	for i in range(10):
		index = random.randint(0, len(lines))
		regex = json.loads(lines[index])['pattern']
		print(regex)
		with open(f"regexes_examples/{i}.txt", 'w') as f:
			print(regex, file=f)


	# with open('uniq-regexes-8.json') as f:
	# 	data = json.load(f)
	# 	print(d)

if __name__ == '__main__':
	main()
