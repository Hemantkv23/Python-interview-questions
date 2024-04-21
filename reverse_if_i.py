def reverse_if_i(input :str) -> str :
    output = ''
    for s in input :
        if s != 'i':
            output += s
        else:
            output = output[::-1]
    return output

print(reverse_if_i('stringi'))