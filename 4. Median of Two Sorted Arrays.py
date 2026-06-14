class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=[]
        j=0
        nums=nums1
        for i in range(len(nums2)):
            nums.append(nums2[i])
        length=len(nums)
        nums.sort()
        if length%2==0:
            mid=length//2
            median=float((nums[mid]+nums[mid-1])/2)
        else:
            mid=length//2
            median=nums[mid]
        return median

sol=Solution()
print(sol.findMedianSortedArrays([1,2],[3,4]))
