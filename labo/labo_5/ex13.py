def print_antipode(coord: tuple) -> None:

    if (-180 <= coord[0] <= 180 and -180 <= coord[1] <= 180):

        lat = 0 - coord[0]

        if coord[1] > 0:
            lon = coord[1] - 180

        else:
            lon = coord[1] + 180

        print(f"Antipode de {coord}:\nLat: {lat}, Long: {lon}")
    else:
        print("Invalide coordinate")


test_1 = (172, 10)
test_2 = (-134, -23)
print_antipode(test_1)
print_antipode(test_2)
