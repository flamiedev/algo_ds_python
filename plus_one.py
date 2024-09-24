from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1
        result = []

        for num in reversed(digits):
            if add > 0 and num == 9:
                result.insert(0, 0)
                add += 1
            elif add > 0:
                result.insert(0, num + 1)
            else:
                result.insert(0, num)

            add -= 1

        if add > 0:
            result.insert(0, 1)

        return result
