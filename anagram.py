def check_anagram(str1, str2):
    dict1 = {}
    dict2 = {}
    for i in str1:
        dict1[i] = dict1.get(i,0) +1
    for j in str2:
        dict2[j] = dict2.get(j,0) +1
    return (dict1==dict2)


def check_anagram2(str1 : str, str2 : str):
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
    return (str1==str2)



print(check_anagram("listen", "silent"))
print(check_anagram2("listen", "silent"))