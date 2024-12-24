def greet():
    return "hello world!"

# Example usage
print(greet())  # Outputs: hello world!

def opposite(number):
    return -number

# Example usage
print(opposite(1))    # Outputs: -1
print(opposite(14))   # Outputs: -14
print(opposite(-34))  # Outputs: 34


def make_negative(number):
    return -abs(number)

# მაგალითები
print(make_negative(1))    # გამოსავალი: -1
print(make_negative(-5))   # გამოსავალი: -5
print(make_negative(0))    # გამოსავალი: 0


def positive_sum(arr):
    return sum(x for x in arr if x > 0)

# მაგალითები
print(positive_sum([1, -4, 7, 12]))  # გამოსავალი: 1 + 7 + 12 = 20
print(positive_sum([-1, -2, -3, -4]))  # გამოსავალი: 0 (დადებითი რიცხვები არ არის)
print(positive_sum([0, 5, -2, 3]))  # გამოსავალი: 5 + 3 = 8


def repeat_str(n, s):
    return s * n

# მაგალითები
print(repeat_str(3, "hello"))  # გამოსავალი: "hellohellohello"
print(repeat_str(5, "a"))      # გამოსავალი: "aaaaa"
print(repeat_str(0, "test"))   # გამოსავალი: ""



