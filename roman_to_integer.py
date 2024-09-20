class Solution:
    def romanToInt(self, s: str) -> int:
        size = len(s)
        value = 0
        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        for i in range(1, size):
            if hashmap[s[i - 1]] < hashmap[s[i]]:
                value -= hashmap[s[i - 1]]
            else:
                value += hashmap[s[i - 1]]

        value += hashmap[s[size - 1]]

        return value
