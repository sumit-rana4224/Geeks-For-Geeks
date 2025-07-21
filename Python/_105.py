"""
You are given a number n. You need to find the sum of digits of n.

Examples :

Input: n = 1
Output: 1
Explanation: Sum of digit of 1 is 1.
Input: n = 99999
Output: 45
Explanation: Sum of digit of 99999 is 45.
Constraints:
1 ≤ n ≤ 107
"""
class Solution:
    def sumOfDigits(self, n):
        x=str(n)
        ret =0
        for i in range(len(x)):
            ret += int(x[i])
        return ret
            
