
# coding: utf-8

# In[3]:

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




# In[4]:

rockpaperscissors(10)


# In[5]:

print(userdata)


# In[6]:

rockpaperscissors(10)


# In[7]:

userdata


# In[8]:

rockpaperscissors(10)


# In[9]:

import numpy as np


# In[10]:

np.array([3, 4, 5, 6])


# In[11]:

np.array([2,2][3,4])


# In[12]:

userdata


# In[13]:

import json


# In[14]:

import json
with open('userdata.txt', 'w') as outfile:
    json.dump(userdata, outfile)


# In[ ]:




# In[15]:

def makearray(data):
    player_data = data.values()
    for i in player_data:
        for k in i:
            data_array = np.array(i)
    
    return data_array


# In[16]:

makearray(userdata)


# In[31]:

makearray(userdata)[3, 2]


# In[2]:

import numpy as np
data_table = np.zeros((10,10))


# In[3]:

data_table[0] = [0, 1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 3.1, 3.2, 3.3]


# In[4]:

data_table[1,0] = 1.1
data_table[2,0] = 1.2
data_table[3,0] = 1.3
data_table[4,0] = 2.1
data_table[5,0] = 2.2
data_table[6,0] = 2.3
data_table[7,0] = 3.1
data_table[8,0] = 3.2
data_table[9,0] = 3.3


# In[5]:

data_table


# In[25]:

for i in data_table:
    for k in i:
        int(k)


# In[27]:

data_table


# In[7]:


won_array = np.zeros((3,3))
lost_array = np.zeros((3,3))
draw_array = np.zeros((3,3))
    


# In[ ]:

def storedata(data, won, lost, draw):
    data_array = makearray(data)

    for i in range(1, len(data_array)):
        if data_array[i-1,3] = 1:
            previous = data_array[i-1,2]
            current = data_array[i,2]
            if previous == current:
                if previous == "rock":
                    won_array[0,0] = previous
                elif previous == "scissors"
                    won_array[1,1] = previous
                else:
                    won_array[]
            
                
        

