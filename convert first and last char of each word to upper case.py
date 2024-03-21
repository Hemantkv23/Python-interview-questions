def convert(s):
    s1 = s[0].upper() + s[1:-1] + s[-1].upper()
    return s1

def convert_up(str1):
    lst = str1.split(" ")
    return ' '.join(convert(i) for i in lst)
       

print(convert_up("hello sir"))
