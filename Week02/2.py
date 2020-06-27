class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return True if list(s).sort()==list(t).sort() else False
        return True if sorted(s)==sorted(t) else False
