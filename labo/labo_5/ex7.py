def print_tails(lst: list) -> None:

    lst_copy = lst.copy()
    for i in range(len(lst_copy)):
        for element in lst_copy:
            print(element)

        del lst_copy[0]


# TEST
test_list_1 = [3, 7, 9]
print(f"Test N°1: {test_list_1}")
print_tails(test_list_1)

test_list_2 = [1, -7, 2]
print(f"Test N°2: {test_list_2}")
print_tails(test_list_2)
