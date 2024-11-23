my_name = "YourName"  # შეცვალეთ თქვენი სახელი

user_name = input("Please enter your name: ")

if user_name == my_name:
    print("Hello")
else:
    print("Bye")


my_favorite_number = 7  # შეცვალეთ თქვენი საყვარელი რიცხვი

user_number = int(input("Please enter your favorite number: "))

if user_number == my_favorite_number:
    print("Perfect")
elif user_number > my_favorite_number:
    print("More")
else:
    print("Less")



for i in range(151):
    if i % 2 == 0:
        print("Luwia", i)
    else:
        print("Kentia", i)


my_name = "YourName"  # შეცვალეთ თქვენი სახელი
my_age = 13  # შეცვალეთ თქვენი ასაკი

user_name = input("Please enter your name: ")
user_age = int(input("Please enter your age: "))

if user_name == my_name and user_age == my_age:
    print("Twins")
else:
    print("Not Twins")



correct_password = "password123"  # შეცვალეთ პაროლი

while True:
    user_password = input("Please enter your account password: ")
    if user_password == correct_password:
        print("Password is correct!")
        break
    else:
        print("Incorrect password, please try again.")
