def multiply_numbers(a, b):
    return a * b

# მაგალითი გამოძახება
result = multiply_numbers(5, 4)
print("ნამრავლი არის:", result)  # 20


s = "Python123"
print(s.isalnum())  # True

s = "12345"
print(s.isdigit())  # True

s = "python"
print(s.islower())  # True

s = "12345"
print(s.isnumeric())  # True

s = "PYTHON"
print(s.isupper())  # True

s = "banana"
print(s.count("a"))  # 3

numbers = [3, 1, 4, 1, 5]
print(min(numbers))  # 1

numbers = [3, 1, 4, 1, 5]
print(max(numbers))  # 5

s = "abcde"
print(min(s))  # 'a'
print(max(s))  # 'e'
