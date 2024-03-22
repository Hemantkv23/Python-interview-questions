def func(num):
    try:
        c = 0
        for i in str(num):
            if num%int(i) != 0:
                return False
        return True
    except ZeroDivisionError:
        return (len(str(num)))

print(func(124))    