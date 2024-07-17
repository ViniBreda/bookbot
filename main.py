def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_char_count(text)
    print_report(num_words, num_chars, book_path)

def print_report(num_words, num_chars : dict, book_path):
    print(f" --- Begin report of {book_path} ---")
    print()
    print(f"{num_words} words found in the document")
    num_chars = dict(sorted(num_chars.items(), key=lambda item: item[1], reverse=True))
    for key in num_chars:
        if key.isalpha():
            print(f"The '{key}' was found {num_chars[key]} times")

    print("--- End report ---")

def get_char_count(book_text):
    book_text = book_text.lower()
    char_count = {}
    for char in book_text:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count

def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()