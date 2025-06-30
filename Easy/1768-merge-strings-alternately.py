# LeetCode Problem: 1768. Merge Strings Alternately
# Level: Easy
# Solved: Yes
# Link: https://leetcode.com/problems/merge-strings-alternately/

class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        i = 0
        j = 0

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result += word1[i]
                i += 1
            if j < len(word2):
                result += word2[j]
                j += 1

        return result

# Explanation:
# We iterate over both strings, appending one character from each alternately.
# If one string ends, we continue with the rest of the other.