# 1) მომხმარებელს შემოატანინეთ მისი ასაკი და გაიგეთ რამდენჯერ მოთავსდება რიცხვი 10 მასში
age = int(input("Enter your age: "))
times_10 = age // 10
print(f"The number 10 fits into your age {times_10} times.")

# 2) მომხმარებელს შემოატანინეთ მისი სახელი და გაიგეთ უდრის თუ არა ის თქვენს სახელს
user_name = input("Enter your name: ")
my_name = "YourName"  # შეცვალეთ თქვენს სახელზე
if user_name == my_name:
    print("Your name matches my name!")
else:
    print("Your name does not match my name.")

# 3) მომხმარებელს შემოატანინეთ ორი რიცხვი (num1 და num2) და გაიგეთ რა იქნება ნაშთი, პირველი რიცხვის მეორეზე გაყოფის შემდეგ
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
remainder = num1 % num2
print(f"The remainder of dividing {num1} by {num2} is {remainder}.")

# 4) მომხმარებელს შემოატანინეთ მისი ასაკი და გაიგეთ არის თუ არა ის ლუწი
age = int(input("Enter your age again: "))
if age % 2 == 0:
    print("Your age is even.")
else:
    print("Your age is odd.")
