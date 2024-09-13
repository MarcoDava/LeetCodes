class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newNums=[0]*len(nums)
        sum=0
        for i in range(len(nums)):
            newNums[i]=nums[i]+sum
            sum+=nums[i]
        return newNums

