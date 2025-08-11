from stats import get_book_wc, get_char_count, sort_char_count  
import sys  

def get_book_text(book_filepath):
    with open(book_filepath) as book:
        print(book.read())

def main():
    if sys.argv.__len__() != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(get_book_wc(sys.argv[1]))
    print("--------- Character Count -------")
    char_count = sort_char_count(get_char_count(sys.argv[1]))
    for char in char_count:
        print(f"{char["char"]}: {char["count"]}")
    print("============= END ===============")
    
main()