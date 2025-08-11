def get_book_wc(book_filepath):
    with open(book_filepath) as book:
        word_count = len(book.read().split())
        return f"Found {word_count} total words"

def get_char_count(book_filepath):
    with open(book_filepath) as book:
        char_count = {}
        for char in book.read():
            if char.lower() not in char_count:
                char_count[char.lower()] = 1
                continue
            char_count[char.lower()] += 1
        return char_count
    
def sort_char_count(char_count):
    char_dict_list = []
    for char in char_count:
        if not char.isalpha():
            continue
        char_dict_list.append({"char": char, "count": char_count[char]})
    char_dict_list.sort(reverse=True, key=lambda x: (x["count"], x["char"]))
    return char_dict_list