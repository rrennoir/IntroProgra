def common_pairs(d1: dict, d2: dict) -> list:

    pairs = []
    for key in d1:
        if key in d2 and d1[key] == d2[key]:
            pairs.append((key, d1[key]))

    return pairs


test_dict_1 = {
    9: "aerfzd",
    3: "dz odbzd",
    "tres": "zndzd",
    4: "nzdnz",
    "z,zd": "zndjz",
    "dzndz": "nzid,z"
}

test_dict_2 = {
    1: "aerfzd",
    3: "dz odbzd",
    "tres": "ndzd",
    5: "nzdnz",
    "z,zd": "zndjz",
    "dzndz": "nzid,z"
}

print(common_pairs(test_dict_1, test_dict_2))
