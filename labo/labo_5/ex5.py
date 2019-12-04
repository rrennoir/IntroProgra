def split_even_odd(lst: list) -> tuple:

    lenght_pair = []
    lenght_impaire = []
    for element in lst:
        if len(element) % 2 == 0:
            lenght_pair.append(element)

        else:
            lenght_impaire.append(element)

    return (lenght_pair, lenght_impaire)


# TEST
test_list_1 = ["GitHub", "ryanr", "Result", "naodznfz"]
print(f"Test N°1: {test_list_1}")
print(f"Result test N°1: {split_even_odd(test_list_1)}\n")

test_list_2 = ["tuple", "attribute", "test", "ybdizfhzijdeubiz"]
print(f"Test N°2: {test_list_2}")
print(f"Result test N°2: {split_even_odd(test_list_2)}\n")
