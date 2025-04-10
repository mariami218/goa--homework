def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "Invalid state"
    

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return [x * i for i in range(1, n + 1)]


def abbrev_name(name):
    first, last = name.split()
    return f"{first[0].upper()}.{last[0].upper()}"



def count_positives_sum_negatives(arr):
    if not arr:  # Check if the array is empty or None
        return []
    
    positive_count = sum(1 for num in arr if num > 0)
    negative_sum = sum(num for num in arr if num < 0)
    
    return [positive_count, negative_sum]


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)