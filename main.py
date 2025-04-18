import sys

from stats import get_word_count, get_char_count, get_sorted_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    word_count = get_word_count(book_content)
    char_dict = get_char_count(book_content)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in get_sorted_char_count(char_dict):
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["count"]}")
    print("============= END ===============")

main()