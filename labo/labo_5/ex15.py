def merge_uniques(lst_from: list, lst_to: list) -> None:

    for element in lst_from:
        if element not in lst_to:
            lst_to.append(element)
            print(f"{element} added")


test1 = [(1, 7, 8, 8), (8, 8, 8, 6), (8, 8, 6)]
test2 = [(8, 8, 8, 6), (8, 7, 8, 6)]

merge_uniques(test1, test2)
