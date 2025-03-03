#1) კომენტარის სახით ახსენით, თუ რა განასხვავებს tuple-ებს List-ებისგან.

#2) შექმენით tuple, რომელიც შეიცავს თქვენს 5 საყვარელ ფილმს, შემდეგ კი დაბეჭდეთ პირველი და ბოლო ელემენტი ამ tuple-დან.

#3) შემენით Tuple, რომელშიც შეინახავთ კვირის დღეებს და მოახდინეთ მათი unpacking (destruction),რათა მიანიჭოთ თითოეული ელემენტი ცალკეულ ცვლადებს და დაბეჭდეთ ეს ცვლადები.

#4) შექმენით tuple, რომელიც შეიცავს რამდენიმე ელემენტს. შემდეგ შეამოწმეთ, შეიცავს თუ არა ეს tuple კონკრეტულ ელემენტს



#N1 
favorite_movies = ("Inception", "Interstellar", "The Dark Knight", "The Matrix", "Shawshank Redemption")
print(favorite_movies[0])  # პირველი ელემენტი
print(favorite_movies[-1]) # ბოლო ელემენტი

#N2
week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

mon, tue, wed, thu, fri, sat, sun = week_days  # Unpacking
print(mon, tue, wed, thu, fri, sat, sun)

#N3
sample_tuple = (10, 20, 30, 40, 50)
element_to_check = 30

if element_to_check in sample_tuple:
    print(f"{element_to_check} არის tuple-ში")
else:
    print(f"{element_to_check} არ არის tuple-ში")




#N4
fruits = ("banana", "cherry", "strawberry", "raspberry")
(first, *second, third) = fruits

print(first)   # პირველი ელემენტი
print(second)  # შუალედური ელემენტები (სია)
print(third)   # ბოლო ელემენტი

#გამოიტანს banana['cherry', 'strawberry'] raspberry
