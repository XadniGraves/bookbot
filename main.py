from stats import get_book_wc, get_char_count    

def get_book_text(book_filepath):
    with open(book_filepath) as book:
        print(book.read())

def main():
    print(get_book_wc("books/frankenstein.txt"))
    char_count = get_char_count("books/frankenstein.txt")
    print (char_count)

main()