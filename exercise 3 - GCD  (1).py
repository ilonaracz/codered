#!/usr/bin/env python
# coding: utf-8

# In[54]:


def dzielnik(a,b):
    
    if a == b:
        return a
        
    elif a > b:
        return fun(a-b,b)
    
    else:
        return fun(a,b-a)

a = 21
b = 63

print(fun(a,b))


# In[11]:


# uwzgledniajac, ze a i b moga miec wartosc 0

def gcd(a,b):
    
    if a == 0:
        return b
    
    if b == 0:
        return a
    
    if a == b:
        return a
        
    if a > b:
        return gcd(a-b,b)
    
    else:
        return gcd(a,b-a)
    
a = 12
b = 12

print('GCD is', gcd(a,b))

