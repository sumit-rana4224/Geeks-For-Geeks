"""
ou are given a string s, you need to print its characters at even indices (index starts at 0).

Examples:

Input: s = "Geeks"
Output: Ges
Explanation: The even indices characters are printed.
Input: s = "DoctorPhenomenal"
Output: DcoPeoea
Explanation: The even indices characters are printed.

"""

class Solution:
    def print_even_indices(self, s: str):
        for i in range(0,len(s),2):
            print(s[i],end='')