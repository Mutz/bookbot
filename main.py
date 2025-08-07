from stats import get_word_count

def get_book_text(path_to_book):
    with open(path_to_book, 'r') as f:
        book_content_text = f.read()
        return book_content_text

if __name__ == '__main__':
    book_text = get_book_text("books/frankenstein.txt")
    print(f"{get_word_count(book_text)} words found in the document")
