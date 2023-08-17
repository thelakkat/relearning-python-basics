#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 22:09:39 2023

@author: thelakkat
https://leetcode.com/problems/palindrome-number/description/
"""

class Solution(object):
    def isPalindrome(self, x):
        Xinword= str(x)
        print(Xinword, " and its length is ", len(Xinword))
        if x<0: return False
        for i in range(len(Xinword)):
            if Xinword[i] != Xinword[len(Xinword)-i-1]:
                return False
            return True
        
print (Solution.isPalindrome(1,-1234321))
