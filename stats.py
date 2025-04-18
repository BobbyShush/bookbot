def get_word_count(book_text):
    text_as_list = book_text.split()
    return len(text_as_list)


def get_char_count(book_text):
    char_dict = {}
    for char in book_text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def get_sorted_char_count(char_dict):
    char_list = []
    for char in char_dict:
        char_list.append({"char":char, "count": char_dict[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list