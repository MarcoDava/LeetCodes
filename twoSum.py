class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a hashset and compare if there are any values from the hashset that equal the number subtracted from the target
        num_to_index = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
               
                return [num_to_index[complement], i]
            num_to_index[num] = i 
        
        
        return []
