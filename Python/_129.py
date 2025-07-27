"""
You are given a code that prints three integers a, b, and c. You need to comment on the line of code that prints the integer b such that this line does not compile.

Note: /* This is a comment */
          // This is also a comment

Examples :

Input: a = 5, b = 6, c = 15
Output: 5 15
Explanation: Only the value of a and c is printed as the line of code that prints b is commented.
Constraints:
1 <= a <= 106
1 <= b <= 106
1 <= c <= 106



"""
class Solution:

    def print_values(self, a, b, c):
        #Code here
        print(a, end=" ")
        # print(b, end=" ")
        print(c, end=" ")
