# LeetCode Problem: 389. Find the Difference
# Level: Easy
# Solved: Yes
# 🔗 https://leetcode.com/problems/find-the-difference/

class Solution(object):
    def findTheDifference(self, s, t):
        sum_s = 0
        sum_t = 0

        for char in s:
            sum_s += ord(char)

        for char in t:
            sum_t += ord(char)

        return chr(sum_t - sum_s)
