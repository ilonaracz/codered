#!/usr/bin/env python
# coding: utf-8

# In[25]:


# 1st method with while 

n=1
while n<101:
    if n%3==0 and n%5==0:
        print (n,'- FizzBuzz')
    elif n%3==0:
        print (n,'- Fizz')
    elif n%5==0:
        print (n, '- Buzz')
    else:
        print (n)
    n=n+1


# In[36]:


# 2nd method with in range

for n in range(1,n+1):
    
    if n % 3 == 0 and n % 5 == 0:
        print(n,'- FizzBuzz')
    
    elif n % 3 == 0:
        print(n,'- Fizz')
        
    elif n % 5 == 0:
        print(n,'- Buzz')
    
    else:
        print(n)
        
n=100
    



# In[50]:


def fizzbuzz(n):

    for n in range(1, n+1):
        
        if n % 3 == 0 and n % 5 == 0:
            print(n,'- FizzBuzz')
        
        elif n % 3 == 0:
            print(n,'- Fizz')
        
        elif n % 5 == 0:
            print(n,'- Buzz')
    
        else:
            print(n)

n=100
fizzbuzz(n)

