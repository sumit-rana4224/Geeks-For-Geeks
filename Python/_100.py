"""
You are given a string s consisting of multiple words. You need to count the total words in the string. Words are separated by a single space.
Note: It is guaranteed that the last character of the given string is not a white space.

Examples:

Input: s = "Geeks"
Output: 1
Input: s = "World is hello"
Output: 3
Constraints:
1 <= |s| <= 104
"""
#User function Template for python3

class Solution:
    def countWords(self,s):
        arr = s.split(" ")
        return len(arr)