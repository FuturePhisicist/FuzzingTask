import os
import random

def generate_malformed_utf8_files(n, size_min, size_max, malformed_chance=0.2, output_dir="malformed_utf8"):
	"""Generates n randomly generated files with malformed UTF-8 sequences."""
	os.makedirs(output_dir, exist_ok=True)

	# Common malformed UTF-8 sequences, thanks Chat
	malformed_bytes = [
		b"\xC0\xAF",  # Invalid 2-byte sequence (overlong encoding)
		b"\xF8\xA1\xA1\xA1\xA1",  # 5-byte sequence (UTF-8 maxes at 4 bytes)
		b"\xE2\x28\xA1",  # Incomplete 3-byte sequence
		b"\x80",  # Lone continuation byte
		b"\xC3",  # Incomplete 2-byte sequence
		b"\xED\xA0\x80",  # UTF-16 surrogate half (invalid in UTF-8)
	]

	for i in range(n):
		file_size = random.randint(size_min, size_max - 1)
		file_path = os.path.join(output_dir, f"malformed_utf8_{i}.txt")

		with open(file_path, "wb") as f:
			written = 0
			while written < file_size:
				if random.random() < malformed_chance:
					corrupt_seq = random.choice(malformed_bytes)
					f.write(corrupt_seq)
					written += len(corrupt_seq)
				else:  # Valid Unicode
					rand_char = chr(random.randint(32, 0x10FFFF))
					encoded = rand_char.encode("utf-8", errors="ignore")
					f.write(encoded)
					written += len(encoded)

		print(f"Generated: {file_path} ({file_size} bytes) with malformed UTF-8")

def main():
	generate_malformed_utf8_files(n=5, size_min=1024, size_max=1 * 1024 * 1024)


if __name__ == '__main__':
	main()

