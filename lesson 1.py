def check_palindrom(str):
    return str == str[::-1]

def check_palindrom2(str):
    for i in range(len(str)):
        if(str[i] != str[-i]):
            return False
    return True
        
print(check_palindrom("aveniseesineva"))
print(check_palindrom("fhgjejgjhb"))

