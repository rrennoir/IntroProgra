def letters_count(word: str) -> dict:

    char_counter = {}
    for char in word:
        if char in char_counter:
            char_counter[char] += 1

        else:
            char_counter.update({char: 1})

    return char_counter


test = "hello"
print(letters_count(test))
