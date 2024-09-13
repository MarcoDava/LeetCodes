class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        stack=[]
        for i in range(len(nums)):
            if nums[i]==target:
                stack.append(i)
        if stack:
            return stack[0],stack[-1]
        else:
            return -1,-1
