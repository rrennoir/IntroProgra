def remove_negatives(lst: list) -> None:

    for element in lst.copy():
        if element < 0:
            index = lst.index(element)
            del lst[index]


# TEST
test_list_1 = [-7, 1, -9, -8, 6, 5, 8, -1]
print(f"Test N°1: {test_list_1}")
remove_negatives(test_list_1)
print(f"Result test N°1: {test_list_1}\n")

test_list_2 = [i for i in range(-5, 5)]
print(f"Test N°2: {test_list_2}")
remove_negatives(test_list_2)
print(f"Result test N°2: {test_list_2}\n")
