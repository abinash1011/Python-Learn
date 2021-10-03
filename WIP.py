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




strs = ["flower","flow","flight"]

commonText = ""
a = min(len(strs[0]), len(strs[1]), len(strs[2]))

for i in range(a):
    if strs[0][i] == strs[1][i] == strs[2][i]:
        commonText += strs[0][i]
    else:
        break
print(commonText)

