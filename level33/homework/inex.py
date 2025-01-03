# 1) სია შექმნა და შეცვლა მითითებების მიხედვით
def modify_list():
    my_list = ["a", "b", "c", "d", "e"]  # საწყისი სია
    my_list.pop(2)  # წაშალე მე-3 ელემენტი (ინდექსი 2)
    my_list.insert(0, "new_element")  # დაამატე ახალი ელემენტი ინდექსზე 0
    return my_list

# 2) ფუნქცია, რომელიც პირველ რიცხვს აიყვანს მეორეს ხარისხში
def power_of(a, b):
    return a ** b

# 3) ფუნქცია, რომელიც ამოწმებს სიის სიგრძის ლუწ ან კენტობას
def check_list_length(my_list):
    if len(my_list) % 2 == 0:
        return "სიის სიგრძე არის ლუწი"
    else:
        return "სიის სიგრძე არის კენტი"
