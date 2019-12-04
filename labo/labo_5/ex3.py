def replace_non_zero(lst: list) -> None:

    for element in lst:
        if element != 0:
            index = lst.index(element)
            lst[index] = 1


# TEST
test_list_1 = [i for i in range(5)]
print(f"Test N°1: {test_list_1}")
replace_non_zero(test_list_1)
print(f"Result test N°1: {test_list_1}")

test_list_2 = []
print(f"Test N°2: {test_list_2}")
replace_non_zero(test_list_2)
print(f"Result test N°2: {test_list_2}")

test_list_3 = ["abc", "zyb", "xyz"]
print(f"Test N°3: {test_list_3}")
replace_non_zero(test_list_3)
print(f"Result test N°3: {test_list_3}")
