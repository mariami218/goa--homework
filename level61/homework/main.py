def filter_list(l):
    result = []
    for item in l:
        if type(item) == int:
            result.append(item)
    return result

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

def find_short(s):
    words = s.split()  # Split the string into words
    l = len(min(words, key=len))  # Find the shortest word and get its length
    return l


def friend(x):
    # შევქმნათ ცარიელი სიები, რომელშიც შევინახავთ მეგობრების სახელებს
    friends = []
    
    # გადავატაროთ ყველა სახელი სიაში
    for name in x:
        # თუ სახელი 4 ასოსგან შედგება, დავამატოთ მეგობართა სიაში
        if len(name) == 4:
            friends.append(name)
    
    # დავუბრუნოთ შედეგი
    return friends


def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))