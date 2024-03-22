def table(i,n):
    for n in range(1,n+1):
        print("{}*{}".format(i,n) + "=" , i*n)
    return True

print(table(3,10))