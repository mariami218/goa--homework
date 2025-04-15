def is_isogram(string):
    string = string.lower()  
    return len(set(string)) == len(string)


def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())


def accum(s):
    result = []
    for index in range(len(s)):
        char = s[index]
        first_letter = char.upper()
        rest = char.lower() * index
        full_piece = first_letter + rest
        result.append(full_piece)
    final_string = '-'.join(result)
    return final_string


def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
    return False


def row_sum_odd_numbers(n):
    start = n * (n - 1) + 1  
    total = 0

    for i in range(n):
        number = start + i * 2  
        total += number

    return total