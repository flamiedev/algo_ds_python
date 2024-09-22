from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur = 0

        for num in nums:
            if num != val:
                nums[cur] = num
                cur += 1

        return cur
