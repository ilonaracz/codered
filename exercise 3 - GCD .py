#!/usr/bin/env python
# coding: utf-8

# In[8]:


def gcd(a,b):
    
    if a == b:
        return a
        
    elif a > b:
        return gcd(a-b,b)
    
    else:
        return gcd(a,b-a)

a = 100
b = 10

print(gcd(a,b))


# In[42]:


# uwzgledniajac, ze a i b moga miec wartosc 0

def gcd(a,b):
    
    if a == 0:
        return b
    
    elif b == 0:
        return a
        
    elif a > b:
        return gcd(a-b,b)
    
    else:
        return gcd(a,b-a)
    
a = 0
b = 12

print('GCD is', gcd(a,b))

