"""
Given a series 9, 33, 73, 129...  Find the n-th term of the series.

Example 1:

Input: n = 4
Output: 129
Explanation: 4th term of the 
series is 129.

Example 2:

Input: n = 5
Output: 201
Explanation: 5th term of the
series is 201.

Your Task:  
You dont need to read input or print anything. Complete the function nthOfSeries() which takes n as input parameter and returns n-th term of the series.

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
1<= n <=104


"""
#User function Template for python3
class Solution:
    def nthOfSeries (self, n):
        x=9
        y=3
        for i in range(n-1):
            x+=8*y
            y+=2
        return x