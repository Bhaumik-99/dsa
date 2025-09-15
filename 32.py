

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]   # Initialize with -1 as base for valid substring
        max_len = 0

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)   # Push index of '('
            else:
                stack.pop()       # Pop last '(' index
                if not stack:
                    stack.append(i)  # Reset base index
                else:
                    max_len = max(max_len, i - stack[-1])  # Update max length

        return max_len

