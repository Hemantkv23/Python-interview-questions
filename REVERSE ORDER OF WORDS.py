sentence = "this is Data Engineer" #input
# output Engineer Data is this

def reverse_sen(sen):
    sentence_lst = sentence.split(" ")
    lst = []
    while len(sentence_lst)>0:
        word = sentence_lst.pop()
        lst.append(word)
    return ' '.join(lst)

print(reverse_sen(sentence))

def reverse_sen1(sen):
    sentence_lst = sentence.split(" ")
    sentence_lst.reverse()
    return ' '.join(sentence_lst)

print(reverse_sen1(sentence))