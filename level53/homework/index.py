fast_food = {"Burger", "Pizza", "Fries", "Hot Dog"}
fast_food.clear()  # ყველა ელემენტის წაშლა
healthy_food = {"Salad", "Fruits", "Vegetables", "Nuts"}
fast_food.update(healthy_food)  # ახალი ელემენტების დამატება
print(fast_food)

def remove_duplicates(lst):
    return list(set(lst))

list1 = [7, 5, 44, 14, 5, 5, 44]
list2 = [89, 90, 56, 45, 90, 78, 90]

print(remove_duplicates(list1))  # [5, 7, 44, 14] (რანდომად დალაგდება)
print(remove_duplicates(list2))  # [89, 90, 56, 45, 78] (რანდომად დალაგდება)
