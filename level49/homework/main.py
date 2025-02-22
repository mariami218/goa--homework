def derive(coefficient, exponent):
    product = coefficient * exponent
    new_exponent = exponent - 1
    return f"{product}x^{new_exponent}"

def get_weekday(number):
    weekdays = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return weekdays.get(number, "Wrong, please enter a number between 1 and 7")

def whatday(num):
    return get_weekday(num)


def create_array(n):
    result = []
    for i in range(1, n + 1):  # Ensure loop starts from 1 to n
        result.append(i)
    return result


def quote(fighter):
    if fighter.lower() == "george saint pierre":
        return "I am not impressed by your performance."
    elif fighter.lower() == "conor mcgregor":
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    else:
        return "Fighter not recognized."
    

def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False
