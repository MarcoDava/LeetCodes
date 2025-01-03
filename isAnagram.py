class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Make hashmap and compare the value amounts of each
        #try not to sort, bad timing complexity
        #convert to hashmap then compare length of the hashmaps
        if len(s)!=len(t):
            return False
        hash_table1={}
        hash_table2={}


        for sindex in s:
            if sindex in hash_table1:
                hash_table1[sindex]+=1
            else:
                hash_table1[sindex]=1
        for tindex in t:
            if tindex in hash_table2:
                hash_table2[tindex]+=1
            else:
                hash_table2[tindex]=1
        
        return hash_table1==hash_table2
    
