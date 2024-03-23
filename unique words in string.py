def unique_words(str1):
    lst1 = []
    dict1 = {}
    for i in str1.split(" "):
        dict1[i] = dict1.get(i,0)+1
    
    for key, value in dict1.items():
        if value == 1:
            lst1.append(key)
    return lst1

print(unique_words("Hello there practicing python there"))