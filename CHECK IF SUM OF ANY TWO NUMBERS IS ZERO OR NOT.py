def check_sum(l):
    if len(l)<2:
        return False
    for i in l:
        if -i in set(l):
            return True
    return False
    
l = [1,2,-2,4,3]

print(check_sum(l))