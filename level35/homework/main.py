def to_jaden_case(strg):
    return ' '.join([word.capitalize() for word in strg.split()])

def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    if (end - begin) % step != 0:
        end -= (end - begin) % step  
    return sum(range(begin, end + 1, step))


def better_than_average(class_points, your_points):
    average = sum(class_points) / len(class_points)
    return your_points > average


def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result


def smash(words):
    return ' '.join(words)



def manual_join(words):
    result = ""
    for i, word in enumerate(words):
        if i > 0:
            result += " "  # Add a space between words
        result += word
    return result
