shopping_list = ("პური", "რძე", "კვერცხი", "ბანანი", "ყველი")
#upacking
item1, item2, item3, item4, item5 = shopping_list

# Fast food პროდუქტების tuple
fast_food = ("ბურგერი", "პიცა", "ფრი")

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

