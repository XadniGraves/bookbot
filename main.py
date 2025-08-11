def get_book_text(book_filepath):
    with open(book_filepath) as book:
        print(book.read())

def get_book_wc(book_filepath):
    with open(book_filepath) as book:
        word_count = len(book.read().split())
        print(f"{word_count} words found in the document")

def main():
    get_book_wc("books/frankenstein.txt")

main()