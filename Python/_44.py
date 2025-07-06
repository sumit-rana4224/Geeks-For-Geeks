"""
"https://www.geeksforgeeks.org/problems/power-of-2-1587115620/1?page=1&difficulty=Easy&sortBy=submissions"


Given a non-negative integer n. You have to check if it is a power of 2 or not. 

Examples

Input: n = 8
Output: true
Explanation: 8 is equal to 2 raised to 3 (23 = 8).
Input: n = 98
Output: false
Explanation: 98 cannot be obtained by any power of 2.
Input: n = 1
Output: true
Explanation: (20 = 1).
Constraints:
0 ≤ n < 109


"""

class Solution:
    def isPowerofTwo(self, n):
        x = 1
        if n == 1:
            return True
        while x <= n:
            x = x*2
            if x == n:
                return True
        return False