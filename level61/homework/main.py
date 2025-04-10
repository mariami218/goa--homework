def filter_list(l):
    result = []
    for item in l:
        if type(item) == int:
            result.append(item)
    return result
