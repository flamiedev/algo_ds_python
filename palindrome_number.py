class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num = x
        reversed_num = 0

        for i in range(len(x)):
            reversed_num = reversed_num * 10 + x % 10
            x = x // 10

        return num == reversed_num
