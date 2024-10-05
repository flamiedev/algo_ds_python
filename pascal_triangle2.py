from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for i in range(1, rowIndex // 2 + 1):
            answer = res[-1] * (rowIndex - i + 1) // i
            res.append(answer)

        if rowIndex == 0:
            return res[:1]
        else:
            if rowIndex % 2 == 0:
                return res[:-1] + res[::-1]
            else:
                return res + res[::-1]
