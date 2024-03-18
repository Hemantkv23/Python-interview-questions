def swap(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b

print(swap(3,4))

def swap2(a,b):
    a,b = b,a
    return a,b

print(swap2(3,4))