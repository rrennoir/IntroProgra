def is_empty(lst: list) -> bool:
    return len(lst) == 0


# TEST
test_list_1 = [i for i in range(5)]
print(f"Test N°1: {test_list_1}")
print_max(test_list_1)

test_list_2 = []
print(f"Test N°2: {test_list_2}")
print_max(test_list_2)
