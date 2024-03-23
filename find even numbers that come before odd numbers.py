def find_even_no(lst):
    return [lst[i] for i in range(0,len(lst)-1) if (lst[i]%2 == 0 and lst[i+1]%2 != 0)]
          


print(find_even_no([1,2,3,4,5,6,7,10,12,14,17,19,20]))