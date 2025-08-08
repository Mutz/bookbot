def get_word_count(text_string):
    word_list = text_string.split()
    return len(word_list)

def get_char_count(text_string):
    lower_case_text = text_string.lower()
    char_dict = {}
    for char in lower_case_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
