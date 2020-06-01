def modfy_produtvion(tile: dict, ressource: str, ammount: int) -> None:

    if (ammount < 0) and (abs(ammount) > tile["production"][ressource]):
        tile["production"][ressource] -= tile["production"][ressource]

    else:
        tile["production"][ressource] += ammount


def new_tile(terrain: str) -> dict:

    if terrain == "water":
        food = 1
        materials = 0
        gold = 0

    elif terrain == "plain":
        food = 2
        materials = 0
        gold = 0

    elif terrain == "forest":
        food = 1
        materials = 1
        gold = 0

    else:
        food = 0
        materials = 2
        gold = 0

    tile = {
        "terrain": terrain,
        "production": {
            "food": food,
            "materials": materials,
            "gold": gold
        },
        "city": None,
        "tradepost": False,
        "owner": None
    }

    return tile


def has_owner(tile: dict, name: str = None) -> bool:

    if tile["owner"] == name:
        return True

    else:
        return False


def has_city(tile: dict) -> bool:
    return tile["city"] is not None


def has_tradepost(tile: dict) -> bool:
    return tile["tradepost"]


def can_build_city(tile: dict) -> bool:
    return (tile["city"]) is None and (tile["terrain"] == "plain")


def can_build_tradepost(tile: dict) -> bool:
    return tile["terrain"] != "water"


def build_tradepost(tile: dict) -> None:

    if tile["terrain"] != "water":
        tile["city"] = None
        tile["tradepost"] = True
        tile["production"]["gold"] += 1

    else:
        print("Can't build tradepost on water!")


def build_city(tile: dict, name: str) -> None:

    if tile["terrain"] == "plain":
        tile["ciy"] = name
        tile["tradepost"] = False
        tile["production"]["gold"] += 3

    else:
        print("Can't build city on anything except plain!")


def cut_forest(tile: dict) -> None:
    if tile["terrain"] == "forest":
        tile["terrain"] = "plain"

    else:
        print("Can't cut anything except forest!")


def change_owner(tile: dict, name: str = None) -> str:
    old_owner = tile["owner"]
    tile["owner"] = name

    return old_owner


def raze_building(tile: dict) -> bool:

    if tile["city"] or tile["tradepost"]:
        tile["city"] = None
        tile["tradepost"] = False
        return True

    else:
        return False


def count_cities(tiles: dict, name: str) -> int:

    city_counter = 0
    for tile in tiles:
        if tile["owner"] == name and tile["city"]:
            city_counter += 1

    return city_counter


def count_total_production(tiles: list, name: str) -> dict:

    total_prod = {
        "food": 0,
        "material": 0,
        "gold": 0
    }
    for tile in tiles:
        if tile["owner"] == name:
            for ressource in tile["production"]:
                total_prod[ressource] += tile["production"][ressource]

    return total_prod
