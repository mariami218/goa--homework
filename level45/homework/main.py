def format_money(amount):
    return f"${amount:.2f}"



def swap_values(args): 
    args[0], args[1] = args[1], args[0]



def same_case(a, b):
    if not a.isalpha() or not b.isalpha():
        return -1
    
    if a.islower() and b.islower() or a.isupper() and b.isupper():
        return 1
    
    return 0


def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    
    max_multiple = (m - 1) // n
    
    return n * max_multiple * (max_multiple + 1) // 2



def multiple_of_index(arr):
    result = [arr[0]] if arr and arr[0] == 0 else []  # ვამატებთ 0-ს, თუ პირველი ელემენტია
    result += [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]
    return result



def calculate_age(birth_year, target_year):
    age_difference = target_year - birth_year
    
    if age_difference == 0:
        return "You were born this very year!"
    
    elif age_difference > 0:
        return f"You are {age_difference} year{'s' if age_difference > 1 else ''} old."
    
    else:
        return f"You will be born in {-age_difference} year{'s' if -age_difference > 1 else ''}."

