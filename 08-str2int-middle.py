#coding = utf-8
import sys
import math

class Solution(object):
    def myAtoi(self, s=str):
        s = s.strip()
        op = 1
        if s == '0' or s == '':
            return 0

        if ('+' in s) and ('-' in s):
             return 0 

        if s[0] == '0' or s[0] == '+':
            op = 1
            s = s[1: ]
        elif s[0] == '-':
            op = -1 
            s = s[1: ]
        else:
            pass

        value = 0
        for i in range(0, len(s)):
            if s[i].isdigit():
                index = ord(s[i]) - ord('0')
                value = value*10 + index
            else:
                break
        resValue = op * value

        maxint = 2147483647
        
        if resValue > maxint: return maxint
        if resValue < -maxint: return -(maxint+1)

        return resValue
