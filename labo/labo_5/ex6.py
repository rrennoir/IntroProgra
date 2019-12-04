def swap_min_first(lst: list) -> None:

    minimum = min(lst)
    min_index = lst.index(minimum)
    first = lst[0]

    lst[0] = minimum
    lst[min_index] = first


# TEST
test_list_1 = [-7, 1, -9, -8, 6, 5, 8, -1]
print(f"Test N°1: {test_list_1}")
swap_min_first(test_list_1)
print(f"Result test N°1: {test_list_1}\n")

test_list_2 = [1, -7, 1, -9, -8, 6, 5, -18, -1]
print(f"Test N°2: {test_list_2}")
swap_min_first(test_list_2)
print(f"Result test N°2: {test_list_2}\n")
