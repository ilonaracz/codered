#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 2. Write a word counter: as input program accepts a txt file, then reads the content from the file 
# and as output prints the number of words in that txt file.
# You need to create this txt file first and fill it with some sentences.
# Example:
# input: Alice in wonderland sleeps
# output: 4

file = open('ex3.txt', 'r')
txt = file.read()
file.close()

words = txt.split()
num_words = len(words)

print(num_words)


# In[15]:


# 5. Rewrite the function from task 4 and now it should return a dictionary 
# with the vowel as key and the number of the vowel in a word as value.

def count_vowels(txt):
    vowels = ["a", "e", "i", "o", "u"]
    count = {letter: txt.lower().count(letter) for letter in vowels if letter in txt.lower()}

    return count

txt = "VOVWELAOEUaauubb"
print(count_vowels(txt))


# In[57]:


# 6. Modify the function created in task 5, but now as input use a 
# csv file with words in it (ie. inputs.csv)

# Expected result: the function should create a txt file with dictionary which contains 
#the input word as key, dictionary with vowels, and the number of the vowels as value. 
#It should look like this: {'banana' : {'a': 3}}

# Example:
# input: file inputs.csv and the content of it:
# banana,vowels

# output: file results.txt and the content of it:
# {'banana' : {'a': 3}}, {'vowels' : {'o': 1, 'e': 1}}


def count_vowels_in_csv(input_csv, output_txt):
    
    with open(input_csv, 'r') as csv_file:
        read_csv = csv.reader(csv_file)
 #       next(read_csv)
        
        with open(output_txt, 'w') as txt_file:
            vowels = ["a", "e", "i", "o", "u"]
            
            for row in read_csv:
                if row:
                    txt = row[0]
                    count = {letter: txt.lower().count(letter) for letter in vowels if letter in txt.lower()}

                    txt_file.write(f"{txt}: {count}")
                                   
    
input_csv = "ex6.csv"
output_txt = "output_ex6.txt"
                                  


# In[54]:


# 7. Write the Morse code translator. Write a function that takes as input
# a string (one word or a sentence) and returns encoded string in the Morse code.

def translate_to_morse(txt):
    morse_dictionary = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '!': '-.-.--', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/':'-..-.', '-':'-....-', ' ': '//'
    }

    txt = txt.upper()
    morse_code = ' '.join([morse_dictionary[char] for char in txt if char in morse_dictionary])

    return morse_code

# Example usage:
input_txt = 'SOS CCC'
result = translate_to_morse(input_txt)

print(result)

