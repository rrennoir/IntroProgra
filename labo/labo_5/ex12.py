def is_palindrome(s: str) -> bool:

    max_i = len(s)
    i = 0
    j = -1
    while (i < max_i) and (s[i] == s[j]):
        i += 1
        j -= 1

    return i == max_i


# TEST
print(is_palindrome("kayak"))
print(is_palindrome("abertyytreza"))
