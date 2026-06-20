class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        else:

            new=0
            c=x
            while x!=0:
                r=x%10
                new=new*10+r
                x=x//10
            if c==new:
                return True
            else:
                return False
