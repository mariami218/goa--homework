def distinct(seq):
    result = []  # ჩამოვაყალიბებთ ცარიელ სიას

    for num in seq:
        if num not in result:  # თუ ელემენტი ჯერ არ გვინახავს
            result.append(num)  # დავამატოთ ის სიაში
    
    return result  # ვაბრუნებთ სიას, რომელიც შეიცავს მხოლოდ უნიკალურ ელემენტებს



def get_planet_name(id):
    # ვქმნით სიას, სადაც პლანეტების სახელებია დალაგებული მზესთან სიახლოვის მიხედვით
    planets = ["Mercury", "Venus", "Earth", "Mars", 
               "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # ვამოწმებთ, რომ მომხმარებელმა შეიყვანა რიცხვი 1-დან 8-მდე
    if 1 <= id <= 8:
        # ვაბრუნებთ შესაბამის პლანეტას სიიდან.
        # რადგან სიის ინდექსაცია იწყება 0-დან, გამოვიყენებთ (id - 1)
        return planets[id - 1]  
    else:
        # თუ შეყვანილი რიცხვი არ არის 1-8 შორის, ვაბრუნებთ ტექსტს, რომ არასწორი მნიშვნელობაა
        return "Invalid planet ID"
    

def switch_it_up(number):
    # ვამოწმებთ რიცხვს და ვაბრუნებთ შესაბამის სიტყვას
    if number == 0:
        return "Zero"
    elif number == 1:
        return "One"
    elif number == 2:
        return "Two"
    elif number == 3:
        return "Three"
    elif number == 4:
        return "Four"
    elif number == 5:
        return "Five"
    elif number == 6:
        return "Six"
    elif number == 7:
        return "Seven"
    elif number == 8:
        return "Eight"
    elif number == 9:
        return "Nine"
    

