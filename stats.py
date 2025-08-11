def get_book_wc(book_filepath):
    with open(book_filepath) as book:
        word_count = len(book.read().split())
        return f"{word_count} words found in the document"

def get_char_count(book_filepath):
    with open(book_filepath) as book:
        char_count = {}
        for char in book.read():
            if char.lower() not in char_count:
                char_count[char.lower()] = 1
                continue
            char_count[char.lower()] += 1
        return dict(sorted(char_count.items()))