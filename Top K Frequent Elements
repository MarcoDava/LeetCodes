class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #initial thought process, use hashmap and compare values to get the k amount of answers
        hash_map = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            hash_map[num]=1+hash_map.get(num,0) 
        for num,cnt in hash_map.items():
            freq[cnt].append(num)
        res = [] 
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
