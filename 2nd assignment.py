#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a program that as input accepts a string typed on keyboard and as output it will print this string reversed
# Example:
# input: Alice in wonderland
# output: dnalrednow ni ecilA


def reversed_string(x):
  return x[::-1]

txt = reversed_string("Alice in wonderland")

print(txt)


# In[57]:


# 4. Write a function that counts the number of vowels in a given word.
# Example 1:
# input: banana
# output: 3
# Example 2:
# input: vowels
# output: 2

def count_vowels(txt):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    count = 0

    for letter in txt:
        if letter in vowels:
            count = count + 1

    return count

txt = "banaaana"
print(count_vowels(txt))
 


# In[75]:


# 3. Write a function to check duplicate letters in words. It must accept strings ie. a sentence.
# The function should return True if any of the words has duplicate letters else return False.
# Example 1:
# input: A cucumber is green
# output: True
# Example 2:
# input: This is it
# output: False
# Example 3:
# input: banana
# output: True

def duplicate_letters(txt):
    words = txt.split()

    return any(len(set(word)) < len(word) for word in words)

txt = "this is it"
result = duplicate_letters(txt)

if result:
    print("True")
else:
    print("False")    


# In[76]:


# 2. Write a word counter: as input program accepts a txt file, then reads the content from the file 
# and as output prints the number of words in that txt file.
# You need to create this txt file first and fill it with some sentences.
# Example:
# input: Alice in wonderland sleeps
# output: 4


