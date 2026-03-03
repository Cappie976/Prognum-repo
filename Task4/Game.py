#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

x = input("choose R, S or P, where R is rock, S is scissors and P is paper " )   #input players choice
y = np.random.choice(['R','S','P'])     #give computer its options to choose from
print(f"computer chooses: {y}")

#conditions to decide winner
if x == 'R' and y == 'S':
    print('you win')
elif x == 'R' and y == 'P':
    print('you lose')
elif x == 'S' and y == 'P':
    print('you win')
elif x == 'S' and y == 'R':
    print('you lose')
elif x == 'P' and y == 'R':
    print('you win')
elif x == 'P' and y == 'S':
    print('you lose')
else:
    print('draw')

