day_number = int(input("Give me the number of the day (1 to 7): "))

# days_name = ("Monday", "Thuesday", "Wenesday", "Thrusday", "Friday", "Saturday", "Sunday")

# if day_number <= 7:
#     print("The {} st/nd/rd/th day is the {}".format(day_number, days_name[day_number - 1]))
# else:
#     print("Incorrecte value.")

if day_number == 1:
    day = "Monday"

elif day_number == 2:
    day = "Thuesday"

elif day_number == 3:
    day = "Wenesday"

elif day_number == 4: 
    day = "Thrusday"

elif day_number == 5:
    day = "Friday"

elif day_number == 6:
    day = "Saturday"

else:
    day = "Sunday"

print("The {} day is {}.".format(day_number, day))
