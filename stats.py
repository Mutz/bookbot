from typing import Dict, List

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

def get_sorted_char_list(char_counts: Dict[str, int]) -> List[Dict[str, int]]:
    """
    Convert a dictionary of character counts into a list of dictionaries
    with keys 'char' and 'num', sorted descending by count.

    Returns:
        List[Dict[str, int]]: e.g., [{'char': 'b', 'num': 4868}, ...]
    """
    items: List[Dict[str, int]] = [{'char': ch, 'num': count} for ch, count in char_counts.items()]
    items.sort(key=lambda d: d['num'], reverse=True)
    return items