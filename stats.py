def get_book_wc(book_filepath):
    with open(book_filepath) as book:
        word_count = len(book.read().split())
        print(f"{word_count} words found in the document")