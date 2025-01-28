def fake_bin(x):
    return ''.join('0' if int(char) < 5 else '1' for char in x)

def remove_char(s):
    return s[1:-1]

def summation(num):
    return sum(range(1, num + 1))
    

def reverse_seq(n):
    return list(range(n, 0, -1))