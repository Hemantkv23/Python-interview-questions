def repeat_chars(str,n):
    s = ''
    for char in str:
        s += char*3
    return s

def repeat_chars_recur(str,n):
    if len(str)==0:
        return ""
    else:
        return str[0]*n+repeat_chars_recur(str[1:],n)


print(repeat_chars('Hello',3))
print(repeat_chars_recur('Hello',3))
