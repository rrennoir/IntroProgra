def is_bissextille(year):

    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True

    return False


def day_in_month(month, year):

    if (month == "Septembre" or month == "Novembre" or
            month == "Avril" or month == "Juin"):
        return 30

    elif month == "Février":
        if is_bissextille(year):
            return 29

        else:
            return 28

    else:
        return 31


print(day_in_month("Février", 2019))
