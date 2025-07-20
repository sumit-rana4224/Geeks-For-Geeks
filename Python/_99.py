"""
Given a series of numbers  3,10,21,36 …., and series starting from N = 1, find the pattern and output the N'th value of the above series.

Example 1:

Input:
N = 1
Output:
3
Explanation:
3 is the first term of the series.
Example 2:

Input:
N = 2
Output:
10
Explanation:
10 is the second term of the series.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function differenceSeries() which takes an integer N as input parameter and returns the N'th term of the series.

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 100

"""
#User function Template for python3

class Solution:
    def differenceSeries(self, N):
        x=3
        y=3
        for i in range(N-1):
            x += y*2+1
            y +=2
        return x