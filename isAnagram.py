class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return Counter(s) == Counter(t)


        from collections import defaultdict
        dic = defaultdict(int)
        for char in s:
            dic[char] += 1
        for char in t:
            dic[char] -= 1
        for v in dic.values():
            if v != 0:
                return False
        return True
        
