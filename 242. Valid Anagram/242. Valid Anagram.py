class Solution:
    def isAnagram(self,s: str,t: str) -> bool:
        hm=defaultdict(str)
        hm=defaultdict(str)
        
        if len(s) != len(t):
            return False
        hm1=sorted(s)
        hm2=sorted(t)
        if hm1==hm2:
            return True
