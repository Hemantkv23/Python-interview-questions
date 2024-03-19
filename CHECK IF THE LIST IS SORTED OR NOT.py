def check_sorted_list(l):
    for i in range(len(l)-1):
        if(l[i]<=l[i+1]):
            continue
        else:
            return False
    return True

print(check_sorted_list([1,2,3,6,5]))

def check_sorted_list1(l):
    return all((l[i]<=l[i+1]) for i in range(len(l)-1))

print(check_sorted_list1([1,2,3,6,5]))
