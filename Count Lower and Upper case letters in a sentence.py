def countLowerUpperCase(str):
     dic = dict()
     for i in str:
        if i.islower():
            dic["lower"] = dic.get("lower",0)+1
        elif i.isupper():
            dic["upper"] = dic.get("upper",0)+1
     return dic


def countLowerUpperCaseLambda(str1):
     dic = dict()
     dic["lower"] = len(list(filter(lambda str1 : str1.islower(), str1)))
     dic["upper"] = len(list(filter(lambda str1 : str1.isupper(), str1)))
     return dic

print(countLowerUpperCase("This is DSA Practice"))
print(countLowerUpperCaseLambda("This is DSA Practice"))



