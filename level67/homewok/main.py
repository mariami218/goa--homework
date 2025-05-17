# 1) Jaden Casing Strings 
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

# 2) Returning Strings 
def greet(name):
    return f"Hello, {name} how are you doing today?"

# 3) Max and Min of List 
def min(lst):
    return sorted(lst)[0]

def max(lst):
    return sorted(lst)[-1]

# 4) Simple Fun #261: Whose Move? 
def whoseMove(lastPlayer, win):
    return lastPlayer if win else ('white' if lastPlayer == 'black' else 'black')

# 5) Simple Comparison? 
def compare(s1, s2):
    if not s1 or not s2:
        return True
    s1 = ''.join([c for c in s1 if c.isalpha()])
    s2 = ''.join([c for c in s2 if c.isalpha()])
    return len(s1) == len(s2)

# დამატებითი 8kyu ამოცანები:

# 6) Opposite number
def opposite(number):
    return -number

# 7) Convert a Boolean to a String
def boolean_to_string(b):
    return str(b)

# 8) Return Negative
def make_negative(number):
    return -abs(number)

# 9) Sum of Positive
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

# 10) String Repeat
def repeat_str(repeat, string):
    return string * repeat

# 11) Remove First and Last Character
def remove_char(s):
    return s[1:-1]

# 12) Find Maximum and Minimum Values of a List
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

# 13) Square(n) Sum
def square_sum(numbers):
    return sum(x**2 for x in numbers)

# 14) Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    if not arr:
        return []
    positives = len([x for x in arr if x > 0])
    negatives = sum(x for x in arr if x < 0)
    return [positives, negatives]

# 15) Reversed Strings
def solution(string):
    return string[::-1]
