"""
Geek is very fond of patterns. Once, his teacher gave him a  pattern to solve. He gave Geek an integer n and asked him to build a pattern.

Help Geek to build a pattern.

 

Example 1:

Input: 5

Output:

*********
 *******
  *****
   ***
    *

Your Task:

You don't need to input anything. Complete the function printTriangle() which takes  an integer n  as the input parameter and print the pattern.

Constraints:

1<= N <= 20
"""
#User function Template for python3

class Solution:
    def printTriangle(self, n):
        x=(n*2)-1
        for i in range(n,0,-1):
            print(" "*(n-i)+"*"*x)
            x -= 2