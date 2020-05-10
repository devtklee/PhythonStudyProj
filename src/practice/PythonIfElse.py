#
# Python If-Else
# Link : https://www.hackerrank.com/challenges/py-if-else/problem?h_r=next-challenge&h_v=zen
# Solved Date : 2020-05-10
# Author : TK Lee
#
# Task
# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format
# A single line containing a positive integer, .
# Constraints
#
# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird.
# Sample Input 0
# 3
# Sample Output 0
# Weird
# Explanation 0
#
#  is odd and odd numbers are weird, so we print Weird.
# Sample Input 1
# 24
# Sample Output 1
# Not Weird
# Explanation 1
#
#  and  is even, so it isn't weird. Thus, we print Not Weird.
#
#

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

if n%2 != 0 :
    print("Weird")
elif n in range (2, 5):
    print ("Not Weird")
elif n in range(6,21):
    print("Weird")
else :
    print("Not Weird")