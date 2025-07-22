"""
Given an integer s, write a program to print the square of size s using "*" character. 
Note: Make sure to add a " " between two "*". Add a new line after printing the square

Examples :

Input: s = 4
Output:
* * * *
*     *
*     *
* * * *
Explanation: It's a square! Each side contains s = 4 *.
Input: s = 3
Output:
* * * 
*   *
* * *
Explanation: It's a square! Each side contains s = 3 *.
Constraints:
1 ≤ s ≤ 10
"""

#User function Template for python3

def square(s):
    for i in range(s):
        for j in range(s):
            if i==0 or i==s-1 or j==s-1 or j==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print('')