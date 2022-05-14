
"""1. Goal Parser"""
"""Input: command = G()(al), Output: Goal """
class Solution:
    def Interpret(self, command):
        return(command.replace("()", "o").replace("(al)", "al"))


Task = Solution()

print("1. " + Task.Interpret('G()(al)'))


"""2. Roman to Integer"""
"""Input: s = III, Output: 3
   Input: s = LVIII, Output: 58
   Input: s = MCMXCIV, Output: 1994"""
class Solution:
    def romanToInt(self, s):
 
        values = {'I': 1, 'V': 5, 'X': 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}   
        result = 0
        for i in range(len(s)):
            if i + 1 == len(s) or values[s[i]] >= values[s[i + 1]] : # if current item is not the last item on the string
                                                                    # or current item's value is greater than or equal to next item's value 
                result = result + values[s[i]]                      # then add current item's value from result
            else:
                result = result - values[s[i]]                      # otherwise subtract current item's value from result
        return result

Task = Solution()
print("2a. ", Task.romanToInt("III"))
print("2b. ", Task.romanToInt("LVIII"))
print("2c. ", Task.romanToInt("MCMXCIV"))


"""3. Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string.
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output:"""
class Solution:
    def longestCommonPrefix(self, strs):
        pass
 
        

Task = Solution()
print(Task.longestCommonPrefix(["flower","flow","flight"]))
print(Task.longestCommonPrefix(["dog","racecar","car"]))
