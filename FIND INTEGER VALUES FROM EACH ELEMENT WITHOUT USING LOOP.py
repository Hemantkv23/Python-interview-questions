def get_num(l):
    lst=[int(i.split(" ")[0]) for i in l]
    return lst

print(get_num(["1 ab","20 ac","4 d"])) 

def get_num1(l):
    lst= list(map(lambda i : int(i.split(" ")[0]),l))
    return lst

print(get_num1(["1 ab","20 ac","4 d"])) 