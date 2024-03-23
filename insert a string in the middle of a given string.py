def replace_str(input_str):
    return input_str.replace('-', '-State:')

def replace_str1(input_str):
    index = input_str.find('-')
    return input_str[:index] + "-State:" + input_str[index+1:]
    


print(replace_str("City:Kolkata-WestBengal"))
print(replace_str1("City:Kolkata-WestBengal"))