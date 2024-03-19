def add(a,b):
    return (a+b)

def sub(a,b):
    return (a-b)

def multiply(a,b):
    return(a*b)

def division(a,b):
    return(a/b)

dic_cal={
    'add':add,
    'sub':sub,
    'multiply':multiply,
    'division':division
}

print(dic_cal['multiply'](3,4))
