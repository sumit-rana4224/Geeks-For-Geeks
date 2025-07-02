"""
"https://www.geeksforgeeks.org/problems/reverse-a-string/1?page=1&difficulty=Basic&sortBy=submissions"

You are given a string s, and your task is to reverse the string.

Examples:

Input: s = "Geeks"
Output: "skeeG"
Input: s = "for"
Output: "rof"
Input: s = "a"
Output: "a"
Constraints:
1 <= s.size() <= 106
s contains only alphabetic characters (both uppercase and lowercase).
"""
#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        return s[::-1]