def get_average(marks):
    return sum(marks) // len(marks)

def points(games):
    total_points=0 
    for game in games:
        x, y = map(int, game.split(":"))
        if x > y: 
            total_points +=3
        elif x == y:
            total_points +=1
            
    return total_points

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

def number(bus_stops):
    passengers = 0
    for on, off in bus_stops:
        passengers += on - off
    return passengers

def generate_shape(n):
    return '\n'.join(['+' * n] * n)

def solution(number):
    total = 0
    for n in range(number):
        if n % 3 == 0 or n % 5 == 0:
            total += n
    return total

def find_it(seq):
    result = 0
    for num in seq:
        result ^= num 
    return result
