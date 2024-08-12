'''Is Subsequence (Leetcode (Easy))

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the
relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false '''

#Solution :

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        else:
            c= ""
            final = ""
            j = 0
            for i in range(len(t)):
                if t[i] == s[j]:
                    c = c+t[i]
                    if j < len(s)-1 :
                        j += 1
            print(c)
            if len(s) == len(c):
                for i in range(len(c)):
                    if s[i] == c[i]:
                        final = final+c[i]
            if final == s:
                return True
