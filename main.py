import sys
from stats import get_num_words, get_char_counts, dict_to_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text) 
    dict_char_count = get_char_counts(book_text)
    list_char_count = dict_to_list(dict_char_count)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for char_row in list_char_count:
        print(f"{char_row['name']}: {char_row['num']}")
    print("============= END ===============")

main()