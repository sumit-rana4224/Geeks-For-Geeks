"""
"https://www.geeksforgeeks.org/problems/decimal-to-binary-1587115620/1?page=10&difficulty=Basic&sortBy=submissions"
Given a decimal number n, return its binary equivalent.

Examples :

Input: n = 12
Output: 1100
Explanation: The binary representation of 12 is "1100", since 12 = 1×23 + 1×22 + 0×21 + 0×20
Input: n = 33
Output: 100001
Explanation: The binary representation of 33 is "100001", since 33 = 1×25 + 0×24 + 0×23 + 0×22 + 0×21 + 1×20
Constraints:
1 ≤ n ≤ 231 - 1


"""

class Solution:
    def decToBinary(self, n):
        binary = str()
        while n :
            temp = n%2
            n=n//2
            binary += str(temp)
        binary = binary[::-1]
        return binary