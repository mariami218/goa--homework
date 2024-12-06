# თავდაპირველი ფასები თითოეულ წიგნზე
book_price_1 = 30  # პირველ წიგნის ფასი
book_price_2 = 45  # მეორე წიგნის ფასი
book_price_3 = 50  # მესამე წიგნის ფასი
book_price_4 = 20  # მეოთხე წიგნის ფასი
book_price_5 = 35  # მეხუთე წიგნის ფასი

# ფასდაკლების ოდენობა პროცენტებში
discount_percentage = 20

# ახალი ფასის გამოთვლა ყოველი წიგნისთვის
discounted_price_1 = book_price_1 - (book_price_1 * discount_percentage / 100)
discounted_price_2 = book_price_2 - (book_price_2 * discount_percentage / 100)
discounted_price_3 = book_price_3 - (book_price_3 * discount_percentage / 100)
discounted_price_4 = book_price_4 - (book_price_4 * discount_percentage / 100)
discounted_price_5 = book_price_5 - (book_price_5 * discount_percentage / 100)

# ახალი ფასების დაბეჭდვა
print("New prices after discount:")
print("Book 1:", discounted_price_1)
print("Book 2:", discounted_price_2)
print("Book 3:", discounted_price_3)
print("Book 4:", discounted_price_4)
print("Book 5:", discounted_price_5)
