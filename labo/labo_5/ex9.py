def str_to_low(s: str) -> str:

    result = ""
    for char in s:
        if char < "a":
            result += chr(ord(char) + 32)

        else:
            result += char

    return result


# TEST
test_1 = "AncFNnczjD"
print(f"Test N°1: {test_1}")
print(f"Result test N°1: {str_to_low(test_1)}\n")

test_2 = "DZKCZKcdzcCCCZBE"
print(f"Test N°2: {test_2}")
print(f"Result test N°2: {str_to_low(test_2)}\n")
