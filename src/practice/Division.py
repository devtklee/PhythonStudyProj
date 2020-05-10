#
# Arithmetic Operators
# Link : https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Solved Date : 2020-05-10
# Author : TK Lee
#
# Task
# Read two integers and print two lines. The first line should contain integer division,  // . The second line should contain float division,  / .
# You don't need to perform any rounding or formatting operations.
# Input Format
# The first line contains the first integer, . The second line contains the second integer, .
# Output Format
# Print the two lines as described above.
# Sample Input 0
# 4
# 3
# Sample Output 0
# 1
# 1.33333333333

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print (round(a/b))
    print(a/b)
