
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = get_word_count(file_contents) 

    count_characters_dict = get_chars_dict(file_contents)

    sorted_dict = get_sorted_dict(count_characters_dict)

    print_report(word_count, sorted_dict)

def get_word_count(text):
    return len(text.split())
    
def get_chars_dict(text):
    chars_dict = {}
    for ch in text:
        if ch.isalpha():
            lowered_ch = ch.lower()
            chars_dict[lowered_ch] = 1 + chars_dict.get(lowered_ch, 0)
    return chars_dict

def get_sorted_dict(char_dict):
    pass


def print_report(count, sorted_dict):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document\n\n")

    for ch in sorted_dict:
        print(f"The '{ch}' character was found {sorted_dict[ch]} times")
    print(f"--- End report ---")

main()  