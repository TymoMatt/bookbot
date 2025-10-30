def get_num_words(file_text):
	all_words = file_text.split()
	return len(all_words)

def get_char_count_dict(file):
	dict = {}
	for char in file:
		char = char.lower()
		if char in dict:
			dict[char] += 1
		else:
			dict[char] = 1
	return dict

def get_sorted_list(dict):
	res = []
	for item in dict:
		full_item = {"char" : item, "num" : dict[item]}
		res.append(full_item)
	res.sort(reverse=True, key=sort_on_num)
	return res

def sort_on_num(items):
	return items["num"]
