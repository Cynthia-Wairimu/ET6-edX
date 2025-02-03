"""

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:


Number of vowels: 5

Your code should not contain a 'input' statement! Further, your code should not define the variable 's'.

"""
#for educational purposes, I will define the variable
s = 'azcbobobegghakl'
#initialize vowel count
vowel_count = 0
#iterate through each char in the string s
for char in s:
    #if the character is a vowel, increment the vowel count
    if char in 'aeiou':
        vowel_count += 1

#print the vowel count
print("Number of vowels: " + str(vowel_count))

