def is_empty(lst: list) -> bool:
    return len(lst) == 0


def print_max(lst: list) -> None:

    if is_empty(lst):
        print("The list is empty!")

    else:
        print(max(lst))


# TEST
test_list_1 = [i for i in range(5)]
print(f"Test N°1: {test_list_1}")
print_max(test_list_1)

test_list_2 = []
print(f"Test N°2: {test_list_2}")
print_max(test_list_2)

test_list_3 = ["abc", "zyb", "xyz"]
print(f"Test N°3: {test_list_3}")
print_max(test_list_3)
