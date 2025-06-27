"""
Given a tuple arr , print "True" if all elements of tuple are different otherwise print "False".

A tuple is a collection of items that are ordered and unchangeable.

Examples:

Input:
arr = (1, 2, 3, 4, 5, 4)
Output: False
Input:
arr = (1, 2, 3, 4, 5)
Output: True
"""

#User function Template for python3
arr = tuple(map(int, input().split()))
lst = []
x=0
alt = 0
while(x<len(arr) and alt ==0):
    if arr[x] in lst:
        alt = 1
    lst.append(arr[x])
    x+=1
    
if alt == 0:
    print('True')
else:
    print("False")