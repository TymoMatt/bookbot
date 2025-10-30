def get_book_text(filepath):
	res = ""
	with open(filepath) as file:
		res = file.read()
	return res


def num_words(file_text):
	all_words = file_text.split()
	num_words = len(all_words)
	print(f"Found {num_words} total words")



def main():
	try:
		file = get_book_text("books/frankenstein.txt")
		num_words(file)
	except Exception as err:
		print("error:" + str(err))


main()
