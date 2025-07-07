"""
"https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops3621/1?page=5&difficulty=Basic&sortBy=submissions"
Given an positive integer n, print numbers from 1 to n without using loops.

Implement the function printTillN() to print the numbers from 1 to n as space-separated integers.

Examples

Input: n = 5
Output: 1 2 3 4 5
Explanation: We have to print numbers from 1 to 5.
Input: n = 10
Output: 1 2 3 4 5 6 7 8 9 10
Explanation: We have to print numbers from 1 to 10.
Constraints:
1 ≤ n ≤ 1000

"""

#User function Template for python3

class Solution:
    
    def printTillN(self, N):
        def count(n,i):
            print(f"{i}",end=' ')
            if i == n:
                return
            return count(n,i+1)
        count(N,1)
            