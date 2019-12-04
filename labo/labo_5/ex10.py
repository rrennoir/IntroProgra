def reverse_str(s: str) -> str:

    reverse_string = ""
    for char in s:
        reverse_string = char + reverse_string

    return reverse_string


# TEST
print(reverse_str("azerty"))
