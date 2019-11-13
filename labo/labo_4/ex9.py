def char_converter(charactere):

    char_unicode = ord(charactere)
    if char_unicode >= 65 and char_unicode <= 90:
        print(chr(char_unicode + 32))

    elif char_unicode >= 97 and char_unicode <= 122:
        print(chr(char_unicode - 32))

    else:
        print("Not a letter between a/A and z/Z")


char_converter("Z")
