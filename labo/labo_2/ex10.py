second_value = int(input("Secondes: "))

minute_value = second_value // 60
hour_value = minute_value // 60
day_value = hour_value // 24
week_value = day_value // 7

day_left = day_value % 7
hour_left = hour_value % 24
minute_left = minute_value % 60
second_left = second_value % 60

print(second_value, "secondes =", week_value, "semaine", day_left, "jours", hour_left, "heures", minute_left, "minutes", second_left, "secondes")