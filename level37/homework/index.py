def array(string):
    sequences = string.split(',')
    
    if len(sequences) <= 2:
        return None
    
    return ' '.join(sequences[1:-1])

def temple_strings(obj, feature): 
    return f"{obj} are {feature}"



def contamination(text, char):
    if not text or not char:
        return ""
    
    return char * len(text)



def is_palindrome(s):
    s = s.lower()
    
    return s == s[::-1]



def obfuscate(email):
    return email.replace('@', ' [at] ').replace('.', ' [dot] ')