# 1) Filter list
def filter_list(l):
    return [i for i in l if isinstance(i, int)]

# 2) Jaden Casing Strings
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

# 3) Sum of Two Lowest Positive Integers
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

# 4) Is this a triangle?
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# 5) Two to One
def longest(a, b):
    return ''.join(sorted(set(a + b)))

# 6) Vowel Count
def getCount(inputStr):
    return sum(1 for c in inputStr if c in "aeiouAEIOU")

# 7) Get the Middle Character
def get_middle(s):
    mid = len(s) // 2
    return s[mid] if len(s) % 2 else s[mid-1:mid+1]

# 8) Find the next perfect square
import math
def find_next_square(sq):
    root = math.isqrt(sq)
    return (root + 1) ** 2 if root * root == sq else -1

# 9) Highest and Lowest
def high_and_low(numbers):
    nums = list(map(int, numbers.split()))
    return f"{max(nums)} {min(nums)}"

# 10) Printer Errors
def printer_error(s):
    return f"{sum(1 for c in s if c not in 'abcdefghijklm')}/{len(s)}"