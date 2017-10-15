
# coding: utf-8

# In[ ]:

def numbigger(S,value):
    bigger_number = []
    for i in S:
        if i > value:
            bigger_number.append(i)
    
    return(len(bigger_number))

