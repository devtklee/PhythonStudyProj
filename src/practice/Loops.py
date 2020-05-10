#
# Arithmetic Operators
# Link : https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Solved Date : 2020-05-10
# Author : TK Lee
#
# Task
# Read an integer . For all non-negative integers , print . See the sample for details.
# Input Format
# The first and only line contains the integer, .
# Constraints
#
# Output Format
# Print  lines, one corresponding to each .
# Sample Input 0
# 5
# Sample Output 0
# 0
# 1
# 4
# 9
# 16

if __name__ == '__main__':
    n = int(input())

    for num in range(0,n):
        print(num**2)

