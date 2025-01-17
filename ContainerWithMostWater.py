class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestVolume=0
        l=0
        r=len(heights)-1
        #two pointer algorithm, use comparison to see the largest combination of area
        while l < r:
            distance = r - l
            if heights[l]>heights[r]:
                if heights[r] * distance > largestVolume:
                    largestVolume=heights[r] * distance
                r-=1
            else:
                if heights[l] * distance > largestVolume:
                    largestVolume=heights[l] * distance        
                l+=1
        return largestVolume
            
