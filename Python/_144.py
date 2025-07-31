"""
Given three numbers a, b, and c. You need to find which is the greatest of them all.

Examples:

Input: a = 1, b = 2, c = 3
Output: 3
Explanation: Clearly, c = 3 is the greatest of (1, 2, 3)
Input: a = 2, b = 2, c = 5
Output: 5
Explanation: Out of (2, 2, 5) 5 is the greatest.
Constraints:
1 <= a, b, c <= 103
"""
#User function Template for python3
# Take a, b and c input and print the greatest of three
lst=[]
lst.append(int(input()))
lst.append(int(input()))
lst.append(int(input()))
print(max(lst))