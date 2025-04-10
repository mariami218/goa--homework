def count_positives_sum_negatives(arr):
    if not arr:  # თუ სია ცარიელია ან None, ვაბრუნებთ ცარიელ სიას
        return []
    
    count_positives = 0
    sum_negatives = 0
    
    for num in arr:
        if num > 0:
            count_positives += 1
        elif num < 0:
            sum_negatives += num
    
    return [count_positives, sum_negatives]

def are_you_playing_banjo(name):
    if name[0] == "R":
        return name + " plays banjo" 
    elif name[0] == "r" :
        return name +" plays banjo" 
    else:
        return name + " does not play banjo"
    

def simple_multiplication(number) :
    # Your code goes here
    return number * 8 if number % 2 == 0 else number * 9

def invert(lst):
    return [-x for x in lst]


def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result




def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


