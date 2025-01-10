class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #initial through process: if the time is O(n), a nested for loop is out of the question
        #thought process after solution: use prefix, suffix method, find the product of numbers before and after number
        n=len(nums)
        prefix=[0]*n
        suffix=[0]*n
        res=[0]*n
        prefix[0]=suffix[n-1]=1
        
        for i in range(1,n):
            prefix[i]=nums[i-1]*prefix[i-1]
            suffix[n-1-i]=nums[n-i]*suffix[n-i]
       
        for i in range(n):
            res[i]=prefix[i]*suffix[i]
        return res
