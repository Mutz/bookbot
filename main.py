import sys
from stats import get_word_count
from stats import get_char_count
from stats import get_sorted_char_list

def get_book_text(path_to_book):
    with open(path_to_book, 'r') as f:
        book_content_text = f.read()
    return book_content_text

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_chars = get_char_count(book_text)
    sorted_char_list = get_sorted_char_list(book_chars)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f" Found {get_word_count(book_text)} total words")
    print(f"--------- Character Count -------")
    for item in sorted_char_list:
        ch = item['char']
        if ch.isalpha():  # print only alphabetic characters
            print(f" {ch}: {item['num']}")
    print(f"============= END ===============")

