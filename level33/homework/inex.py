# 1) სია შექმნა და შეცვლა მითითებების მიხედვით
def modify_list():
    my_list = ["a", "b", "c", "d", "e"]  # საწყისი სია
    my_list.pop(2)  # წაშალე მე-3 ელემენტი (ინდექსი 2)
    my_list.insert(0, "new_element")  # დაამატე ახალი ელემენტი ინდექსზე 0
    return my_list

# 2) ფუნქცია, რომელიც პირველ რიცხვს აიყვანს მეორეს ხარისხში
def power_of(a, b):
    return a ** b

# 3) ფუნქცია, რომელიც ამოწმებს სიის სიგრძის ლუწ ან კენტობას
def check_list_length(my_list):
    if len(my_list) % 2 == 0:
        return "სიის სიგრძე არის ლუწი"
    else:
        return "სიის სიგრძე არის კენტი"

# 4) ფუნქცია 1: You Can't Code Under Pressure #1
def double_integer(i):
    return i * 2

# 5) ფუნქცია 2: Friend or Foe?
def friend_or_foe(names):
    return [name for name in names if len(name) == 4]

# 6) ფუნქცია 3: Beginner - Reduce but Grow
def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result

# 7) ფუნქცია 4: Is n divisible by x and y?
def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0

# 8) ფუნქცია 5: Pipe Problem
def pipe_fix(nums):
    return list(range(nums[0], nums[-1] + 1))

# 9) ფუნქცია 6: String ends with?
def solution(string, ending):
    return string.endswith(ending)

# 10) ფუნქცია 7: Sorting by last character
def sort_me(words):
    return sorted(words, key=lambda word: word[-1])

