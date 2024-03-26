class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        n = len(s)
        l = 0
        r = n-1
        while l<r :
            if s[l] != s[r]:
                # excluding s[l] and including s[r]
                one = s[l+1:r+1] 
                # excluding s[r] and including s[l]
                two = s[l:r]
                return (one == one[::-1]) or (two == two[::-1])
            l+=1
            r-=1
        return True
    
obj = Solution()
print(obj.validPalindrome("lcupuuffuupucul")  )  
# confusion comes whether to exclude s[l] or s[r]