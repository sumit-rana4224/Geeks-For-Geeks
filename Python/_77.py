"""
Given a string s, the task is to change the complete string to uppercase or lowercase depending on the case of the first character.

Examples:

Input: s = "abCD"
Output: "abcd"
Explanation: The first letter (a) is lowercase. Hence, the complete string is made lowercase.
Input: s = "Abcd"
Output: "ABCD"
Explanation: The first letter (A) is uppercase. Hence, the complete string is made uppercase.
Constraints:
1<=|s|<=104
"""
#User function Template for python3


class Solution:
    def modify(self, s):
        x=s[0]
        if s[0] == x.upper():
            return s.upper()
        else :
            return s.lower()