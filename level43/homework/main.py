def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    return sum(range(begin, end + 1, step))

def filter_list(lst):
    return [x for x in lst if isinstance(x, int)]


def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

def sum_mix(arr):
    return sum(int(x) for x in arr)

def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)

def reverse_words(string):
    return ' '.join(string.split()[::-1])

def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))

