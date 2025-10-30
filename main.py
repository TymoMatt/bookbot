from stats import print_num_words
from stats import get_char_count_dict

def get_book_text(filepath):
	res = ""
	with open(filepath) as file:
		res = file.read()
	return res

def main():
	try:
		file = get_book_text("books/frankenstein.txt")
		print_num_words(file)
		dict = get_char_count_dict(file)
		for item in dict:
			count = dict[item]
			print(f"'{item}': {count}")
	except Exception as err:
		print("error:" + str(err))


main()
