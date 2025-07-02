"""
"https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?page=1&difficulty=Basic&sortBy=submissions"

Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

Examples:

Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
Output: true
Explanation: b[] is a subset of a[]
Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
Output: true
Explanation: b[] is a subset of a[]
Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
Output: false
Explanation: b[] is not a subset of a[]
Constraints:
1 <= a.size(), b.size() <= 105
1 <= a[i], b[j] <= 106



"""
#User function Template for python3

# class Solution:
#     def isSubset(self, a, b):
#         # for i in range(len(b)):
#         #     if b[i] in a:
#         #         a.remove(b[i])
#         #     else:
#         #         return False
#         # return True

from collections import Counter

class Solution:
    def isSubset(self, a, b):
        count_a = Counter(a)
        count_b = Counter(b)
        
        for key in count_b:
            if count_b[key] > count_a.get(key, 0):
                return False
        return True

                