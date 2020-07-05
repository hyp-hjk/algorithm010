class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        if len(s)==0 or len(g)==0 or s[-1]<g[0]:return 0
        gi=si=count=0
        while gi<len(g) and si<len(s):
            if s[si]>=g[gi]:
                count+=1
                s[si]=0
                gi+=1
            si+=1
        return count