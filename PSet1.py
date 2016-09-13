# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 10:47:52 2016

@author: David
"""

#
# Count the number of vowels in 
# all lowercase string s
#

count = 0
for char in s: 
    if char in 'aeiou': count += 1
print('Number of vowels: ' + str(count))

#%%

#
# Count all occurrences of 'bob' in
# string s
#

bobcount = 0
for i in range(len(s)-2):
    if s[i:i+3] == 'bob': bobcount += 1
print("Number of times bob occurs is: " + str(bobcount))

#%%

#
# Takes string s (all-lowercase) as input and
# identifies the longest alphabetically-ordered
# substring
#

substring, longest = s[0], s[0]
for char in s[1:]:
    substring += char
    if substring[-1] < substring[-2]: substring = char
    if len(longest) < len(substring): longest = substring
print("Longest substring in alphabetical order is: " + longest)