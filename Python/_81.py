"""
As we have seen, the System.out.println() statement automatically appends a new line to our output. Here, we'll learn how to prevent that.
You are given two string variables a and b, and you have to print a and b with a space between them. However, you must prevent the print statement from providing a new line as the new line will be given by the main driver code.

Examples:

Input: a = "Hello", b = "World"
Output: "Hello World"
Explanation: a and b are printed in a single line and a space separates them.The new line is provided by the driver code.

"""
#User function Template for python3
a = input()
b = input()

print(a+" "+b)