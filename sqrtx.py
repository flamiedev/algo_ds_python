class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x

        while start <= end:
            middle = (start + end) // 2

            if middle * middle == x:
                return middle
            elif middle * middle > x:
                end = middle - 1
            else:
                start = middle + 1

        return end
