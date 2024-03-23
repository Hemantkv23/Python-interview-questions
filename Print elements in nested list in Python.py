def elements_in_nested_list(lst):
     list1 = []
     for i in lst:
         if(type(i)==list):
            list1 += i
     return (list1)

def elements_in_nested_list1(lst):
     list1 = []
     for i in lst:
         if(isinstance(i,list)):
            list1 += i
     return (list1)
        
lst_elements = [1,2,3,['Sam','Ravish'],45,[432,'Jailer'],43,'Sam']
print(elements_in_nested_list(lst_elements))
print(elements_in_nested_list1(lst_elements))