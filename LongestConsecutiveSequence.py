class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #initial thought process, O(n) solution transferring into a hashset and using a for loop that asks if the next number exists
        # hash_set=set(nums)
        # Sequence=1
        # longestSequence=0
        # startingNums=[]
        # for num in hash_set:
        #     if not (num - 1 in hash_set) and num+1 in hash_set:
        #         startingNums.append(num)
        # if(len(startingNums)==0):
        #     return 1
        # index=0
        # num=startingNums[index]
        # while num < max(nums):
        #     print(num)
        #     if num+1 in hash_set:
        #         Sequence+=1
        #     else:
        #         if Sequence>longestSequence:
        #             longestSequence=Sequence
        #             Sequence=1
        #             index+=1
        #             num=startingNums[index]
        #     num+=1
        # return longestSequence

        numSet=set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length=1
                while(num + length) in numSet:
                    length+=1
                longest = max(length,longest)
        return longest
        
