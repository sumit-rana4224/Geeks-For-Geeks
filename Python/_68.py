"""
"https://www.geeksforgeeks.org/problems/check-palindrome--141628/1?page=15&difficulty=Basic&sortBy=submissions"

Given a string s, you need to check if it is palindrome or not.

A palidrome is a string that reads the same from front and back.

Note: Ignore the case in this question.

Examples:

Input: s = "Hello"
Output: false
Explanation: Hello is not equal to olleH so it's not a palindrome.
Input: s = "TenEt"
Output: true
Explanation: TenEt == tEneT as we are ignoring the case.

"""
#User function Template for python3
def isPalindrome(s):
     s =s.lower()
     return s == s[::-1]