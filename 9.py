class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            # Build reversed half of the number
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # A palindrome if the left half == right half (or without middle digit for odd-length numbers)
        return x == reversed_half or x == reversed_half // 10


