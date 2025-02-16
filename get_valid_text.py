import os
import random

def generate_utf8_files(n, size_min, size_max, output_dir="valid_utf8"):
	"""Generates n randomly generated UTF-8 files of random sizes within [size_min, size_max)."""
	os.makedirs(output_dir, exist_ok=True) 

	for i in range(n):
		file_size = random.randint(size_min, size_max - 1)
		file_path = os.path.join(output_dir, f"random_utf8_{i}.txt")

		with open(file_path, "w", encoding="utf-8") as f:
			written = 0
			while written < file_size:
				rand_char = chr(random.randint(32, 0x10FFFF))  # UTF-8 valid characters
				if rand_char.isprintable() or rand_char in "\n\t":
					f.write(rand_char)
					written += len(rand_char.encode("utf-8"))  # Count actual bytes

		print(f"Generated: {file_path} ({file_size} bytes)")

def main():
	generate_utf8_files(n=5, size_min=1024, size_max=1 * 1024 * 1024)

if __name__ == '__main__':
	main()
