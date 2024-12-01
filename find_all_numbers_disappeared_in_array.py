class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length : int = len(nums)
        seen : list[bool] = [False] * length 
        for num in nums:
            seen[num-1] = True
        return [i+1 for i in range(length) if not seen[i]]
