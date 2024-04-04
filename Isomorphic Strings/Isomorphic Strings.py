class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        zipped = set(zip(s,t))
        if len(zipped) == len(set(s)) == len(set(t)):
            return True
        else:
            return False

obj = Solution()
print(obj.isIsomorphic("egg","add"))
