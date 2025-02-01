"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print
Longest substring in alphabetical order is: abc

"""
#initialize the variables
longest = '' #Stores the longest substring in alphabetical order
current = s[0] #tarts with the first character of the string s

#iterate through each character in the string s
for i in range(1, len(s)):
    #if the current character is greater than or equal to the previous character, add it to the current substring
    if s[i] >= s[i-1]:
        current += s[i]
    else:
        #if the current substring is longer than the longest substring, update the longest substring
        if len(current) > len(longest):
            longest = current
        #start a new current substring
        current = s[i]
        
#After the loop, check if the last current substring is longer than the longest substring
if len(current) > len(longest):
    longest = current
    
#print the longest substring
print("Longest substring in alphabetical order is: " + longest)

