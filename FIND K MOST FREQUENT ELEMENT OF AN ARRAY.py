def k_most_element(l,n):
    final_dic = dict()
    final_set = set()
    for i in l:
        if i in final_dic:
            final_dic[i] += 1
            if(final_dic[i]>=n):
                final_set.add(i)
        
        else:
            final_dic[i] = 1
    return final_set

print(k_most_element([1,1,1,2,2,3,4,4,5,5,5,5],3))
