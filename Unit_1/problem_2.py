"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl',
then your program should print

Number of times bob occurs is: 2
"""

#initialize count of 'bob' substrings
bob_count = 0

#iterate through each character in the string s
for i in range(len(s) - 2):  #stop 2 characters before the end of the string to avoid out of bounds error.
    #if the substring of the next 3 characters is 'bob', increment the bob count
    if s[i:i+3] == 'bob':
        bob_count += 1
        
#print the bob count
print("Number of times bob occurs is: " + str(bob_count))