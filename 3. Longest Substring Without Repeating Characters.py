class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            new_s=set()
            for j in range(i,len(s)):
                if s[j] in new_s:
                    break;
                new_s.add(s[j])
                ans=max(ans,j-i+1)
        return ans
sol=Solution()
ans=sol.lengthOfLongestSubstring("abcabcbb")
print(ans)
