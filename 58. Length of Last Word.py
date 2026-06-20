class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=0
        s=s.strip()
        for i in range(-1,-len(s)-1,-1):
           
                

            if s[i]==" ":
                return length
            else:
                length+=1
        return length
