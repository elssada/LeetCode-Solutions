class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count=0
        current_count=0

        for num in nums:
            if num==1:
             current_count+=1      #update max_count if current_count is higher 
             max_count= max(max_count, current_count)
            else:
             current_count=0 #This will reset our streak if the next num is not 1
        return max_count
