def sort_key(d: dict) -> tuple:

    sorted_int_dict = {}
    sorted_str_dict = {}

    for key in d:
        if type(key) == int:
            sorted_int_dict.update({key: d[key]})

        elif type(key) == str:
            sorted_str_dict.update({key: d[key]})

    return (sorted_int_dict, sorted_str_dict)


test_dict = {
    1: "aerfzd",
    3: "dz odbzd",
    "tres": "zndzd",
    4: "nzdnz",
    "z,zd": "zndjz",
    "dzndz": "nzid,z"
}

print(sort_key(test_dict))
