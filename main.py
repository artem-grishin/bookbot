
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = get_word_count(file_contents) 

    count_characters_dict = get_chars_dict(file_contents)

    char_count_sorted_list = get_sorted_list(count_characters_dict)

    keys, values = get_keys_values(count_characters_dict)

    print_report(word_count, char_count_sorted_list, keys, values)

def get_word_count(text):
    return len(text.split())
    
def get_chars_dict(text):
    chars_dict = {}
    for ch in text:
        if ch.isalpha():
            lowered_ch = ch.lower()
            chars_dict[lowered_ch] = 1 + chars_dict.get(lowered_ch, 0)
    return chars_dict

def get_sorted_list(char_dict):
    sorted_list = sorted(list(char_dict.values()), reverse=True)
    return sorted_list

def get_keys_values(char_dict):
    key_list = list(char_dict.keys())
    value_list = list(char_dict.values())
    return (key_list, value_list)

def print_report(count, sorted_list, keys, values):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document\n\n")

    for ch in sorted_list:
        print(f"The '{keys[values.index(ch)]}' character was found {ch} times")
    print(f"--- End report ---")

main()  