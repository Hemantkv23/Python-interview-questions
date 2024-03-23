def find_key(dic,value):
    return [k for k, v in dic.items() if(v>value)]

def find_key1(dic,value):
    return list(dict(filter(lambda x:x[1]>value, dic.items())).keys())


my_map={
    'a': 150,
    'b': 75,
    'c': 200,
    'd': 50,
    'e': 300
}

print(find_key(my_map,100))
print(find_key1(my_map,100))
        