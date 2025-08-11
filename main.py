from stats import get_book_wc

def get_book_text(book_filepath):
    with open(book_filepath) as book:
        print(book.read())

def main():
    get_book_wc("books/frankenstein.txt")

main()