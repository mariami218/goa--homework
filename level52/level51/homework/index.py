shopping_list = ("პური", "რძე", "კვერცხი", "ბანანი", "ყველი")
#upacking
item1, item2, item3, item4, item5 = shopping_list
print(item1)
print(item2)
print(item3)
print(item4)
print(item5)

fast_food = ("burger", "fries", "coke")  # თავდაპირველი tuple
fast_food = list(fast_food)  # გარდაქმნა list-ად

fast_food[0] = "salad"  # პირველი ელემენტი იცვლება
fast_food[1] = "water"  # მეორე ელემენტი იცვლება
fast_food[2] = "fruits"  # მესამე ელემენტი იცვლება

print(tuple(fast_food))  # ისევ tuple-ში გარდაქმნა და ბეჭდვა

# Tuple-ი უცვლადია, ამიტომ ახალს ვქმნით ჯანსაღი საკვების დამატებით
healthy_food = ("სალათი", "ავოკადო", "თევზი")

# Tuple-ების გაერთიანება
new_food_tuple = fast_food + healthy_food
print(new_food_tuple)

fruits = ("ვაშლი", "მსხალი", "ბანანი", "ატამი")
(first, *middle, last) = fruits

print(first)   # "ვაშლი"
print(middle)  # ["მსხალი", "ბანანი"]
print(last)    # "ატამი"

months = ("January", "February", "March", "April", "May")
(first, second, third, *fourth) = months

print(first)   # "January"
print(second)  # "February"
print(third)   # "March"
print(fourth)  # ["April", "May"]

#January  February  March ['April', 'May'] 

