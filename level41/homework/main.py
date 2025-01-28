def converter(mpg):
    """
    Convert miles per imperial gallon to kilometers per liter.

    Args:
        mpg (float): Miles per imperial gallon.

    Returns:
        float: Kilometers per liter rounded to two decimal places.
    """
    MILES_TO_KM = 1.609344
    GALLON_TO_LITERS = 4.54609188

    kpl = (mpg * MILES_TO_KM) / GALLON_TO_LITERS
    return round(kpl, 2)



def plural(n):
    return n != 1


def hello(name=""):
    if not name:
        return "Hello, World!"
    else:
        # Capitalize the first letter and lowercase the rest of the name
        return f"Hello, {name.capitalize()}!"


def check(seq, elem):
    return elem in seq

def hex_to_dec(s):
    return int(s, 16)

