# 1) Dictionary და სიების შექმნა
my_dict = {"name": "Mariami", "age": 25, "city": "Tbilisi"}

keys_list = []
values_list = []

for key, value in my_dict.items():
    keys_list.append(key)
    values_list.append(value)

print("Keys:", keys_list)
print("Values:", values_list)


# 2) დუბლიკატების მოშორება სიიდან
result = [10, 43, 12, 11, 94, 10, 55, 7, 11]
unique_result = list(set(result))

print("Unique List:", unique_result)


# 3) Python მეთოდების მაგალითები

# 1. append()
lst = [1, 2, 3]
lst.append(4)
print(lst)  # [1, 2, 3, 4]

# 2. pop()
removed = lst.pop()
print(lst)  # [1, 2, 3]
print(removed)  # 4

# 3. sort()
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # [1, 2, 5, 9]

# 4. reverse()
numbers.reverse()
print(numbers)  # [9, 5, 2, 1]

# 5. count()
print(numbers.count(5))  # 1


# 4) მომხმარებლის შეყვანის dictionary-ის შექმნა
user_dict = {}

key = input("Enter key: ")
value = input("Enter value: ")

user_dict[key] = value

print("Current Dictionary:", user_dict)

new_value = input(f"Enter new value for {key}: ")
user_dict[key] = new_value

print("Updated Dictionary:", user_dict)


# 5) Set-ის მსგავსი ფუნქცია (დუბლიკატების მოცილება)
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
clean_list = remove_duplicates(numbers_with_duplicates)
print("List without duplicates:", clean_list)