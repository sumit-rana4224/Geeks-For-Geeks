"""
"https://www.geeksforgeeks.org/problems/remainder-evaluation3755/1?page=11&difficulty=Basic&sortBy=submissions"
Given two positive integers n1 and n2, the task is to find the remainder when n1 is divided by n2.

Examples:

Input: n1 = 5, n2 = 3
Output: 2
Explanation: The remainder after dividing 5 by 3 is: 2.
Input: n1 = 5, n2 = 10
Output: 5
Explanation: 5 cannot be divided by 10 so it is the Remainder.
Constraints:
0 <= n1 <= 106
1 <= n2 <= 106
"""

#User function Template for python3

class Solution:
    def findRemainder(self, n1, n2):
    	return n1%n2