"""
"https://www.geeksforgeeks.org/problems/sort-the-array0055/1?page=3&difficulty=Basic&sortBy=submissions"

Given a random array arr of numbers, please return them in ascending sorted order. 

Examples:

Input: arr[] = [1, 5, 3, 2]
Output: [1, 2, 3, 5]
Explanation: After sorting array will be like [1, 2, 3, 5].
Input: arr[] = [3, 1]
Output: [1, 3]
Explanation: After sorting array will be like [1, 3].
Input: arr[] = [1, 2, 3]
Output: [1, 2, 3]
Explanation: It's already in expected form.
Constraints:
1 ≤ arr.size ≤ 105
1 ≤ arr[i] ≤ 105


"""
#User function Template for python3
class Solution:
    def sortArr(self, arr): 
        return arr.sort()