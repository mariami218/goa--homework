def ends_with(string, suffix):
    return string.endswith(suffix)


def sum_of_cubes(n):
    return sum(i**3 for i in range(1, n + 1))


def sort_array(arr):
    if arr is None or len(arr) == 0:
        return []
    return sorted(arr)