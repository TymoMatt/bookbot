def print_num_words(file_text):
	all_words = file_text.split()
	num_words = len(all_words)
	print(f"Found {num_words} total words")

def get_char_count_dict(file):
	dict = {}
	for char in file:
		char = char.lower()
		if char in dict:
			dict[char] += 1
		else:
			dict[char] = 1
	return dict
