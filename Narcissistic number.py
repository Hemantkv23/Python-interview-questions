def check_narcissistic(num):
    str1 = str(num)
    sum1=0
    for i in str1:
        sum = 1
        count = len(str1)
        while count>0:
            sum = sum*int(i)
            count=count-1
        sum1 += sum
    return (sum1 == num)

def check_narcissistic2(num):
    sum1=0
    for i in str(num):
        sum1 += int(i) ** len(str(num))
    return (sum1 == num)

print(check_narcissistic(1634))
print(check_narcissistic2(1634))
        

