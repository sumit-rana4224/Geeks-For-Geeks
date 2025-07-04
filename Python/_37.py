"""
"https://www.geeksforgeeks.org/problems/odd-or-even3618/1?page=2&difficulty=Basic&sortBy=submissions"

Given a positive integer n, determine whether it is odd or even. Return true if the number is even and false if the number is odd.

Examples:

Input: n = 15
Output: false
Explanation: The number is not divisible by 2, Odd number.
Input: n = 44
Output: true
Explanation: The number is divisible by 2, Even number.
Constraints:
1 ≤ n ≤ 104

"""

class Solution:
    def isEven (self, n):
        # tell = [True,False]
        # return tell[n%2]
        return n%2 == 0