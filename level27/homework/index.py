def sum_numbers(a, b):
    print(a + b)

# გამოძახება
sum_numbers(5, 7)  # 12

def is_even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# გამოძახება
print(is_even_or_odd(10))  # even
print(is_even_or_odd(7))   # odd

def is_positive_or_negative(number):
    if number >= 0:
        return "positive"
    else:
        return "negative"

# გამოძახება
print(is_positive_or_negative(15))  # positive
print(is_positive_or_negative(-8))  # negative

def greet(name):
    print(f"Hello {name}!")

# გამოძახება
greet("mariam")  # Hello mariam!
greet("Nino")    # Hello Nino!

def concatenate_strings(string1, string2):
    return string1 + string2

# გამოძახება
result = concatenate_strings("Hello ", "World!")
print(result)  # Hello World!

