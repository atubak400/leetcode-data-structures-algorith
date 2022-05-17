
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
        result = ""
        
        for i in range(len(strs[0])):                       # Pick any word in the list and loop through its length. Thats the number of times youre to loop thu the list
                                                            # because your answer cant be longer in length than any word in the list
            for word in strs:                                  # loop through the words in the the list so you can use the word[i] to acces the letters of each word                
                if i == len(word) or word[i] != strs[0][i]:     # stop code by returning result if loop count(i) is same as length of your chosen word 
                    return "".join(result)                               # or if theres no more similar between other words and your chosen word
            result = result + strs[0][i]                        # otherwise keep adding the similar letters that occur in same position in all the words to the result 
 
        

Task = Solution()
print("3a. ",Task.longestCommonPrefix(["flower","flow","flight"]))
print("3b. ",Task.longestCommonPrefix(["dog","racecar","car"]))

#or

class Solution:
    def longestCommonPrefix(self, strs):
        result = []
        for i in zip(*strs):
            if len(set(i)) != 1:
                break
            result.append(i[0])
        return "".join(result)     

"""The zip() method returns a zip object, which is an iterator of tuples where 
the first item in each passed iterator is paired together, and then the second item in 
each passed iterator are paired together etc.
If the passed iterators have different lengths, the iterator with the least items 
decides the length of the new iterator.

set() method is used to convert any of the iterable to sequence of iterable elements 
with distinct elements, commonly called Set. 
"""                 
 
        

Task = Solution()
print("3a. ",Task.longestCommonPrefix(["flower","flow","flight"]))
print("3b. ",Task.longestCommonPrefix(["dog","racecar","car"]))
