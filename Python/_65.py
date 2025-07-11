"""
"https://www.geeksforgeeks.org/problems/geek-and-coffee-shop5721/1?page=13&difficulty=Basic&sortBy=submissions"
Given two values N and M. Give the value when N is halved M-1 times.

Example 1:

Input: N = 100, M = 4
Output: 12
Explaination: The sequence of numbers is 
100, 50, 25, 12.
Example 2:

Input: N = 10, M = 5
Output: 0
Explaination: The sequence is 10, 5, 2, 1 and 0.
Your Task:
You do not need to read input or print anything. Your task is to complete the function mthHalf() which takes N and M as input  parameters and retunrs the value of N when it is halved M-1 times.

Expected Time Complexity: O(log(max(N, M)))
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 109
1 ≤ M ≤ 1000


"""
#User function Template for python3

class Solution:
    def mthHalf(self, N, M):
        if M==0:
            return 0
        for i in range(M-1):
            N=N//2
        return N