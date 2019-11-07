day_number = int(input("Give me the number of the day (1 to 7): "))

days_name = ("Monday", "Thuesday", "Wenesday", "Thrusday", "Friday", "Saturday", "Sunday")

if day_number <= 7:
    print("The {} st/nd/rd/th day is the {}".format(day_number, days_name[day_number - 1]))
else:
    print("Incorrecte value.")