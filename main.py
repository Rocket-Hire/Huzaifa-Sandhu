#
# Given a function which takes an array of strings as input, find the longest common prefix string amongst the array of strings.

# If there is no common prefix, return an empty string "".
# Example 1:

# Input: strs = ["browser","brother","brand"]
# Output: "br"

# Example 2:

# Input: strs = ["cat","dog","zebra"]
# Output: ""

def longest_prefix(arr):
  temp = arr[0]
  # match = ''
  match_index = 0
  mat = False
  for i in range(len(temp)):
    if mat == True:
      match_index = i
    for x in range(1,len(arr)):
      word = arr[x]
      if temp[i] == word[i]:
        mat = True
      else:
        mat  = False

    return temp[:match_index]
        
strs = ["browser","brother","brand"]
print(longest_prefix(strs))


    
# Question: Grouping anagrams

# Write a function which takes an array of strings strs and groups the anagrams together.
# Anagram is formed by rearranging the letters of different words. See the examples below
# You do not have to worry about optimizing for time complexity in this question but overall time complexity will be discussed at the end.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

["aet","aet","ant","aet","ant","abt"]

Employee Table
EmpId  FirstName LastName JoinedOn 
1      Huzaifa   Sandhu   1/1/2023 
2      Omer       Khan   1/1/2023 

Inventory
InventoryId  InventoryName   IssuedTo   IssuedOn
1            Mouse A          1          1/2/2023
2            Mouse B          1          1/2/2023
3            Mouse C          2          1/2/2023
4            Mouse D          1          1/2/2023


select FirstName,LastName,InventoryId,InventoryName,IssuedOn
from Inventory
innerjoin Employee on EmpId = InventoryId