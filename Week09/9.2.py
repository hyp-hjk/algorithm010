class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        size = len(a)
        if size < k:
            return s[::-1]
        l, r = 0, size
        for i in range(0, size, 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)