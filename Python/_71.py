"""
"https://www.geeksforgeeks.org/problems/java-reverse-a-string0416/1?page=4&difficulty=Basic&sortBy=submissions"

Given a string s , return reverse of the string as output.

Example 1:

Input: 
s = "GeeksforGeeks"
Output: "skeeGrofskeeG" 
Explanation: Reverse string of "GeeksforGeeks" will be "skeeGrofskeeG"
Example 2:

Input: 
s = "ReversE"
Output: "EsreveR"
Explanation: Reverse string of "ReversE" will be "EsreveR"

Your Task:  
You dont need to read input or print anything. Complete the function revStr() which takes s as input parameter and returns the reversed string .

Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(|s|)

Constraints:
1<= |s| <=106
"""
#User function Template for python3
class Solution:
    def revStr (self, s : str) -> str :
        return s[::-1]