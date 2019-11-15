def char_converter(charactere):

    char_unicode = ord(charactere)
    if 65 <= char_unicode <= 90:
        print(chr(char_unicode + 32))

    elif 97 <= char_unicode <= 122:
        print(chr(char_unicode - 32))

    else:
        print("Not a letter between a/A and z/Z")


char_converter("Z")
char_converter("z")
char_converter("A")
char_converter("a")
char_converter("f")
