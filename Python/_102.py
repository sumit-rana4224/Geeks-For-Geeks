"""
Calculate factorial of a given number N.
 

Example 1:

Input: 5
Output: 120
Explanation: 1 * 2 * 3 * 4 * 5 = 120.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function find_fact() which takes n as input parameter and returns factorial of N.
 

Expected Time Complexity: O(N)
Expected Space Complexity: O(1)
 

Constraints:
1 <= N <= 18


"""
#User function Template for python3

class Solution:
    def find_fact(self, n):
        f=1
        for i in range(1,n+1):
            f *=i
        return f