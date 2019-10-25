second_value = int(input("Secondes: "))

minute_value = second_value // 60
hour_value = minute_value // 60

minute_left = minute_value % 60
second_left = second_value % 60

print(second_value, "secondes =", hour_value, "heures", minute_left, "minutes", second_left, "secondes")