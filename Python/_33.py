"""
"https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&difficulty=Easy&sortBy=submissions"

You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

Examples:

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.
Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.
Input: arr[] = [1]
Output: 2
Explanation: Only 1 is present so the missing element is 2.
Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ arr.size() + 1

"""
class Solution:
    def missingNum(self, arr):
        # max_num = max(arr)
        # if max_num == len(arr):
        #     return max_num+1
        # else:
        #     for i in range(max_num):
        #         if i+1 not in arr:
        #             return i+1
        # return
        n = max(arr)
        ts = (n*(n+1))//2
        ars = sum(arr)
        if ts-ars == 0:
            return n+1
        return ts-ars