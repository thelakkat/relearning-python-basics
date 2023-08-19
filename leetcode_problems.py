#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 22:09:39 2023

@author: thelakkat
https://leetcode.com/problems/palindrome-number/description/

Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""
# --------string method --------------
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
# --------string method --------------

# --------non-string method --------------

class Solution(object):
    def isPalindrome1(self, x):
        if x<0: return False
        myArray=[]
        while x>0:
            myArray.append(x%10)
            print ("this is my array ",myArray)
            x = x//10
            print("this is the new X ", x) 
            if x == 0: break
        for i in range(len(myArray)):
            if myArray[i] != myArray[len(myArray)-i-1]: return False
        return True
        
print (Solution.isPalindrome1(1,12321))