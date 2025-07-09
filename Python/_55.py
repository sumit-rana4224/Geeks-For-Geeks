"""
"https://www.geeksforgeeks.org/problems/sum-of-digits1742/1?page=6&difficulty=Basic&sortBy=submissions"

Given a positive number n. Find the sum of all the digits of n.

Examples:

Input: n = 687
Output: 21
Explanation: Sum of 687's digits: 6 + 8 + 7 = 21
Input: n = 12
Output 3
Explanation: Sum of 12's digits: 1 + 2 = 3
Constraints:
1 <= n <= 105


"""

class Solution:
    def sumOfDigits(self, n):
        sum = 0
        x=n
        while x != 0:
            sum += x%10
            x=x//10
        return sum