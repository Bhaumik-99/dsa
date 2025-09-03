class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        # Start with the first term
        result = "1"
        
        for _ in range(n - 1):
            temp = ""
            i = 0
            
            while i < len(result):
                count = 1
                
                # Count consecutive identical digits
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1
                
                # Append count and digit to temp
                temp += str(count) + result[i]
                i += 1
            
            result = temp  # Update result for the next iteration
        
        return result
