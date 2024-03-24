def find_common(str1 : str, str2 : str):
    lst = []
    set1 = set(str1)
    set2 = set(str2)
    print("all letter :",set1 | set2)
    print("common letters: ",set1 & set2)
    print("present in first but not in second: ",set1 - set2)
    print("present in second but not in first: ",set2 - set1)

str1 = "Hemant Kumar Verma"
str2 = "Data Engineer"
print(find_common(str1, str2))