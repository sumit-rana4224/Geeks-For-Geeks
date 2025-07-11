"""
"https://www.geeksforgeeks.org/problems/table-difference/1?page=12&difficulty=Basic&sortBy=submissions"
Given two number n1 and n2, n1 > n2. Find the differences between mathematical tables of n1 and n2 and print in a single line.
Note: Don't add a new line in the end.

Example :

Input: n1 = 9, n2 = 4
Output: 5 10 15 20 25 30 35 40 45 50 
Explanation:
  9 18 27 36 45 54 63 72 81 90
- 4  8 12 16 20 24 28 32 36 40
-----------------------------------------
= 5 10 15 20 25 30 35 40 45 50
Input: n1 = 6, n2 = 2
Output: 5 10 15 20 25 30 35 40 45 50 
Explanation:
  6 12 18 24 30 36 42 48 54 60
- 2  4  6  8 10 12 14 16 18 20
-----------------------------------------
= 4  8 12 16 20 24 28 32 36 40
Constraints:
1  ≤  n1 , n2  ≤  106
"""
#User function Template for python3
import numpy as np
def difference(n1,n2):
    l1 =[]
    l2 = []
    for i in range(1,11):
        l1.append(i*n1)
        l2.append(i*n2)
    arr1 = np.array(l1)
    arr2 = np.array(l2)
    diff =arr1-arr2
    for i in diff:
        print(i,end=" ")
    

#User function Template for python3
import numpy as np
def difference(n1,n2):
    arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
    arr2 = np.array([1,2,3,4,5,6,7,8,9,10])
    arr1 *= n1
    arr2 *= n2
    diff =arr1-arr2
    for i in diff:
        print(i,end=" ")
    