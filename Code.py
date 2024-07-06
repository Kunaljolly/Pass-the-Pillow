class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        t = list(range(1,n+1))
        if time<n:
            return t[time]
        if (time//(n-1))%2 == 0:
            return t[time%(n-1)]
        return n-(time%(n-1))
