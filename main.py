from stats import get_num_words
from stats import get_char_count_dict
from stats import get_sorted_list

def get_book_text(filepath):
	res = ""
	with open(filepath) as file:
		res = file.read()
	return res

def print_title(filepath):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}")

def print_word_count(file):
	print("----------- Word Count ----------")
	num_words = get_num_words(file)
	print(f"Found {num_words} total words")

def print_char_count(dict):
	print("--------- Character Count -------")
	li = get_sorted_list(dict)
	for item in li:
		if item["char"].isalpha():
			print(f"{item["char"]}: {item["num"]}")
	print("============= END ===============")

def main():
	try:
		filepath = "books/frankenstein.txt"
		print_title(filepath)

		file = get_book_text(filepath)
		dict = get_char_count_dict(file)

		print_word_count(file)

		print_char_count(dict)

	except Exception as err:
		print("error:" + str(err))


main()
