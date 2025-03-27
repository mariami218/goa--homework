# მანქანის აღწერის დიქშენერი
car = {
    "brand": "BMW",
    "model": "M5",
    "year": 2023
}

# გასაღებები და მნიშვნელობები წყვილად
print(car.items())  
# [('brand', 'BMW'), ('model', 'M5'), ('year', 2023)]

# გასაღებები ცალ-ცალკე
print(car.keys())  
# dict_keys(['brand', 'model', 'year'])

# მნიშვნელობები ცალ-ცალკე
print(car.values())  
# dict_values(['BMW', 'M5', 2023])



# ორი სეტი
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# გაერთიანება (union)
union_set = set1 | set2
print("Union:", union_set)
# Output: {1, 2, 3, 4, 5, 6, 7, 8}

# მსგავსება (intersection)
intersection_set = set1 & set2
print("Intersection:", intersection_set)
# Output: {4, 5}

# განსხვავება (difference)
difference_set = set1 - set2
print("Difference:", difference_set)
# Output: {1, 2, 3}


person = {
    "name": "Nika",
    "age": 25,
    "city": "Tbilisi"
}

# `for` ციკლით მნიშვნელობების ამოღება
for value in person.values():
    print(value)


# დიქშენერი (Dictionary) არის მონაცემთა სტრუქტურა, რომელიც ინახავს გასაღებ-მნიშვნელობის (key-value) წყვილებს.
# გასაღებები უნიკალურია და მათი გამოყენებით შეგვიძლია მნიშვნელობებზე წვდომა.

# სეტი (Set) არის ელემენტების კოლექცია, სადაც თითოეული ელემენტი უნიკალურია.
# მასში არ მეორდება ერთნაირი ელემენტები და არ აქვს ინდექსირებული წვდომა.
