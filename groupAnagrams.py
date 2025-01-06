class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #initial thought process, make a hashmap within a hashmap and save the indexes of each word in the key.
        res = defaultdict(list)
        for word in strs:
            count=[0]*26
            for letter in word:
                count[ord(letter) - ord ("a")] += 1#ascii value for arithmetic
            res[tuple(count)].append(word)

        return res.values()
