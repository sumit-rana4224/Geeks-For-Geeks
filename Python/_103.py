"""
Given a string s, extract all the integers from s.

Example 1:

Input:
s = "1: Prakhar Agrawal, 2: Manish Kumar Rai, 
     3: Rishabh Gupta56"
Output: 1 2 3 56
Explanation: 
1, 2, 3, 56 are the integers present in s.
Example 2:

Input:
s = "geeksforgeeks"
Output: No Integers
Explanation: 
No integers present in the string.
 

Your Task:
You don't need to read input or print anything. Complete the function extractIntegerWords() which takes string s as input and returns a list of strings. If an empty list is returned the output is printed as "No Integers".

 

Expected Time Complexity: O(|s|).
Expected Auxiliary Space: O(|s|).

 

Constraints:
1<=|s|<=105


"""
#User function Template for python3
import re
class Solution:

    def extractIntegerWords(self, s):
        x=re.findall(r'\d+',s)
        return x