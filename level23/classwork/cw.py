"N1"

# ტექსტი, რომელზეც ვიმუშავებთ
text = "Hello, Python!"

# 1. lower() - სტრიქონის ყველა ასოს გადაყვანა პატარა ასოებში
lower_text = text.lower()  
# "Hello, Python!" გახდება "hello, python!"
print(lower_text)  # შედეგი: hello, python!

# 2. upper() - სტრიქონის ყველა ასოს გადაყვანა დიდი ასოებში
upper_text = text.upper()  
# "Hello, Python!" გახდება "HELLO, PYTHON!"
print(upper_text)  # შედეგი: HELLO, PYTHON!

# 3. capitalize() - მხოლოდ პირველი ასოს გადაყვანა დიდ ასოში, დანარჩენი პატარა ასოებად
capitalized_text = text.capitalize()  
# "Hello, Python!" გახდება "Hello, python!"
print(capitalized_text)  # შედეგი: Hello, python!

# 4. find() - მოძებნის სტრიქონში მითითებული ქვეთექსტის პირველი აღმოჩენის ინდექსს
position = text.find("Python")  
# "Python" იწყება მე-7 ინდექსზე (ინდექსაცია იწყება 0-დან)
print(position)  # შედეგი: 7


"N2"
# მომხმარებლის გვარის შეყვანა
surname = input("შეიყვანეთ თქვენი გვარი: ")

# გვარის პირველი ასოს შემოწმება
if surname[0].upper():
    print("Hello")
else:
    print("Bye")

"N3"
# მომხმარებლის სახელის შეყვანა
name = input("შეიყვანეთ თქვენი სახელი: ")

# ასოს შეყვანა, რომელიც უნდა მოიძებნოს
char = input("შეიყვანეთ ასო: ")

# ასოს მოძებნა სახელში
if char in name:
    print(f"found it: {name.find(char)}")  # ინდექსის ჩვენება
else:
    print("Can't find character")


"N4"
# მომხმარებლის გვარის შეყვანა
surname = input("შეიყვანეთ თქვენი გვარი: ")

# მომხმარებლის არჩევანის შეყვანა
choice = input("როგორ უნდა შეიცვალოს თქვენი გვარის ასოები? (upper/lower/capitalize): ")

# არჩევანის მიხედვით მოქმედება
if choice == "upper":
    print(surname.upper())
elif choice == "lower":
    print(surname.lower())
elif choice == "capitalize":
    print(surname.capitalize())
else:
    print("მიუთითეთ სწორი არჩევანი (upper/lower/capitalize).")










