class Solution:
    def trap(self, height: List[int]) -> int:
        highestLeft=0
        highestRight=0
        l=0
        r=len(height)-1
        totalArea=0
        while l < r:
            if highestLeft<highestRight:
                if height[l]>highestLeft:
                    highestLeft=height[l]
                else:
                    totalArea+=min(highestLeft,highestRight)-height[l]
                    l+=1
            else:
                if height[r]>highestRight:
                    highestRight=height[r]
                else:
                    totalArea+=min(highestLeft,highestRight)-height[r]
                    r-=1
        return totalArea



