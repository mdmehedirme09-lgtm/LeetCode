class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            sign=1
        else:
            sign=-1
        x=abs(x)
        y=0
        r=0
        while x!=0:
            r=x%10
            y=y*10+r
            x=x//10
        y=y*sign
        if y<-2**31 or y>2**31-1:
            return 0
        return y

sol=Solution()
print(sol.reverse(123))
            
       
            
            
          
     
           
         
          
         
         
    
        
         

      
    
        
    

        
      
 




