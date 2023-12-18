def get_weekday(day_number):
    weekdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
    }

    if day_number > 4:
        return weekdays[0]

    return weekdays[day_number]