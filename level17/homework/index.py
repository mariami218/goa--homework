# 1) შექმენით სია შემდგარი 5 ელემენტისგან და გამოიტანეთ ამ სიის თითოეული ელემენტი ინდექსებით
my_list = ["apple", "banana", "cherry", "date", "elderberry"]
for i in range(len(my_list)):
    print(f"Element at index {i}: {my_list[i]}")

# 2) შექმენით სია შემდგარი 10 ელემენტისგან და გამოიტანეთ თითოეული ელემენტი for ციკლით / range() ფუნქციითაც და პირდაპირ ცვლადის გადაცემითაც
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# range() ფუნქციის გამოყენებით
for i in range(len(my_list)):
    print(f"Using range(): {my_list[i]}")

# პირდაპირ ცვლადის გადაცემით
for element in my_list:
    print(f"Direct iteration: {element}")

# 3) შექმენით სია შემდგარი რიცხვებისგან, გადაუარეთ for ციკლით და გამოიტანეთ მხოლოდ ის რიცხვები რომელიც მეტია 10ზე
number_list = [5, 12, 7, 18, 3, 21, 9]
for number in number_list:
    if number > 10:
        print(f"Number greater than 10: {number}")

# 4) შექმენით სია შემდგარი 7 განსხვავებული ემენეტისგან და for ციკლის მეშვეობით შეამოწმეთ თითოეული ემენეტის მონაცემთა ტიპი
mixed_list = [42, "hello", 3.14, True, None, [1, 2, 3], {"key": "value"}]
for element in mixed_list:
    print(f"Element: {element}, Type: {type(element)}")
