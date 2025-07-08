"""
"https://www.geeksforgeeks.org/problems/triangle-number-1661489840/1?page=6&difficulty=Basic&sortBy=submissions"

Geek is very fond of patterns. Once, his teacher gave him a  pattern to solve. He gave Geek an integer n and asked him to build a pattern.

Help Geek to build a pattern.

 

Example 1:

Input: 5

Output:
1 2 3 4 5
1 2 3 4
1 2 3 
1 2  
1 

 

Your Task:

You don't need to input anything. Complete the function printTriangle() which takes  an integer n  as the input parameter and print the pattern.

Constraints:

1<= N <= 20

"""

#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(N,0,-1):
            for j in range(1,i+1):
                print(j,end=" ")
            print("")