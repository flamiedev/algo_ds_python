import sys


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(0)
        if len(num1) + len(num2) > 600:
            return str(int(num1) + int(num2))
        return str(int(num1) + int(num2))
