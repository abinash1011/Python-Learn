# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 
# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.



import random 
strs = ["flower","flow","flight","flush"]

word_len_in_strs = [len(i) for i in strs]

shortest_word_len = min(word_len_in_strs)

commonText = ""

for index_words, words in enumerate(strs):
    
    
































#len_list = []

# for word in strs:
#     len_list.append(len(word))
# min_length_of_Word = min(len_list)

# for i in range(min_length_of_Word):
#     if strs[0][i] == strs[1][i] == strs[2][i]:
#         commonText += strs[0][i]
#     else:
#         break
# print(commonText)

