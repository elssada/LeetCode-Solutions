class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]

        for i in range(n):
           ans.append(nums[i]) #To grab a number from x
           ans.append(nums[i+n]) #To grab a number from Y
           
        return ans