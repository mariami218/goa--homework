# მომხმარებლის სახელის შეყვანა
name = input("Enter your name in uppercase: ")  # ვთქვათ, მომხმარებელი წერს "mariami"
name = name.lower()
print("Name in lowercase:", name)  # შედეგი იქნება: "mariami"

surname = "tsereteli"  # გვარი პატარა ასოებით
surname = surname.upper()
print("Surname in uppercase:", surname)  # შედეგი: "wavwavadze"

string = "hello world"  # პატარა ასოებით სტრინგი
string = string.capitalize()
print("Capitalized string:", string)  # შედეგი: "Hello world"

text = "programming"
letter = 'g'
index = text.find(letter)
print(f"The index of '{letter}' is:", index)  # შედეგი: 3

strings = ["apple", "banana", "cherry"]
uppercase_strings = []

for s in strings:
    uppercase_strings.append(s.upper())

print("Uppercase strings:", uppercase_strings)  # შედეგი: ["APPLE", "BANANA", "CHERRY"]
