
# coding: utf-8

# In[5]:

import random

def choice(user):
    your_choice = input('Rocks, paper, scissors! Which one do you choose? [r/p/s]:')
    if your_choice == 'r':
        return 'rock'
    elif your_choice == 'p':
        return 'paper'
    elif your_choice == 's':
        return 'scissors'
    else:
        return 'invalid choice! Try again!'
        choice(user)

userdata = dict()

def rockpaperscissors(N):
    name = input('what is your name? ')
   
    if name in userdata.keys():
        return 'you already played!'
    else:
        userdata[name] = []
    
        start = 1
        while start != N+1:
            r = random.choice(['rock','paper','scissors'])
            x = choice(name)

            if x is r:
                userdata[name].append((start, r, x, 0))
                start = start + 1
                print('draw')
            if x is 'rock':
                if r is 'paper':
                    userdata[name].append((start, r, x, -1))
                    start = start + 1
                    print('loss')
                if r is 'scissors':
                    userdata[name].append((start, r, x, 1))
                    start = start + 1
                    print('win')
            if x is 'scissors':
                if r is 'rock':
                    userdata[name].append((start, r, x, -1))
                    start = start + 1
                    print('loss')
                if r is 'paper':
                    userdata[name].append((start, r, x, 1))
                    start = start + 1
                    print('win')
            if x is 'paper':
                if r is 'rock':
                    userdata[name].append((start, r, x, 1))
                    start = start + 1
                    print('win')
                if r is 'scissors':
                    userdata[name].append((start, r, x, -1))
                    start = start + 1
                    print('loss')
    
    return userdata[name]


# In[ ]:




# In[6]:

rockpaperscissors(10)


# In[11]:

print(userdata)


# In[12]:

rockpaperscissors(10)


# In[13]:

userdata


# In[14]:

rockpaperscissors(10)


# In[7]:

import numpy as np


# In[8]:

np.array([3, 4, 5, 6])


# In[10]:

np.array([2,2][3,4])


# In[11]:

userdata


# In[12]:

import json


# In[14]:

import json
with open('userdata.txt', 'w') as outfile:
    json.dump(userdata, outfile)


# In[15]:




# In[25]:

def makearray(data):
    player_data = data.values()
    for i in player_data:
        for k in i:
            data_array = np.array(i)
    
    return data_array


# In[26]:

makearray(userdata)


# In[33]:

makearray(userdata)[2, 2]


# In[53]:

data_table = np.zeros((10,10))


# In[54]:

data_table[0] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# In[57]:

data_table[1,0] = 1
data_table[2,0] = 2
data_table[3,0] = 3
data_table[4,0] = 4
data_table[5,0] = 5
data_table[6,0] = 6
data_table[7,0] = 7
data_table[8,0] = 8
data_table[9,0] = 9


# In[58]:

data_table


# In[66]:

for i in data_table:
    for k in i:
        int(k)


# In[67]:

data_table


# In[ ]:



