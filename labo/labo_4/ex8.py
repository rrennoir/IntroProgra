def day_in_month(month, bissextile="Non"):

    if (month == "Septembre" or month == "Novembre" or
            month == "Avril" or month == "Juin"):
        return 30

    elif month == "Février":
        if bissextile == "Non":
            return 28

        else:
            return 29

    else:
        return 31
