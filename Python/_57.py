"""
"https://www.geeksforgeeks.org/problems/triangle-pattern-1661718013/1?page=7&difficulty=Basic&sortBy=submissions"
Geek is very fond of patterns. Once, his teacher gave him a pattern to solve. He gave Geek an integer n and asked him to build a pattern.

Help Geek to build a star pattern.

Example 1:

Input: 5
Output:
* 
* * 
* * * 
* * * * 
* * * * *
* * * *
* * *
* *
*
Example 2:

Input: 3
Output:
* 
* * 
* * * 
* *
*
Your Task:
You don't need to input anything. Complete the function printTriangle() which takes an integer n  as the input parameter and prints the pattern.

Expected Time Complexity: O(n2).
Expected Auxiliary Space: O(1).

Constraints:
1 <= n <= 1000


"""
#User function Template for python3

class Solution:
    def printTriangle(self, n):
        for i in range(1,n+1):
            for j in range(i):
                print('*',end =" ")
            print('')
        for i in range(n-1,0,-1):
            for j in range(i):
                print('*',end =" ")
            print('')
        
                