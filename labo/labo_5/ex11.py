import time
import random


def count_chars(chars: str, s: str) -> int:

    char_counter = 0
    for char in chars:
        for char_s in s:
            if char == char_s:
                char_counter += 1

    return char_counter


# TEST
print(count_chars("ajnz", "bczbcqoicauibefuaicuapaiavvjeixcnzfinfziofzvpvc"))
