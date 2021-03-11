
    
    
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # single char is palindrom
        # s[i:j] is palindrom is s[i+1:j-1] is palindrom and s[i] == s[j]
        
        palindrom = [[False] * len(s) for _ in range(len(s))]
        start, end = 0,0
        # set single char as palindrom
        for i in range(len(s)):
            palindrom[i][i] = True
            
        # as we need to know i+1 and j-1, we will set the outer loop with j
        for j in range(len(s)):
            for i in range(0, j+1):
                # when s[i] and s[j] are same.
                # if length is <= 2, then s[i:j] is palindrom
                # if length is > 2, then only if s[i+1:j-1] is palindrom
                if s[i] == s[j] and (j-i+1 <= 2 or (j-i+1 > 2 and palindrom[i+1][j-1])):
                    palindrom[i][j] = True
                    
                    if end-start+1 < j-i+1:
                        start, end = i,j

        return s[start:end+1]
