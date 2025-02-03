"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl',
then your program should print

Number of times bob occurs is: 2
"""
#for educational purposes, I will define the variable
s = 'azcbobobegghakl'

#initialize count of 'bob' substrings
bob_count = 0

#iterate through each character in the string s
for i in range(len(s) - 2):  #stop 2 characters before the end of the string to avoid out of bounds error. 
    #When searching for a substring of length N, your loop should stop N-1 characters before the end of the string.
    #for example, when searching for a substring of length 3, N=3, so the loop should stop at 3-1=2
    
    #if the substring of the next 3 characters is 'bob', increment the bob count
    #When searching for a substring of length, use index-based loops instead of character-based loops.
    if s[i:i+3] == 'bob': # Extracts 3 characters (perfect for "bob") starting from index i excluding the character at index i+3
        bob_count += 1
        
#print the bob count
print("Number of times bob occurs is: " + str(bob_count))

