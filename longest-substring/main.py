from collections import Counter


class Solution:
    def divide_and_conquer(self, s: str, k: int, start: int, end: int) -> int:
        if start == end:
            return 0

        counter = Counter()

        for i in range(start, end + 1):
            counter[s[i]] += 1

        for i in range(start, end + 1):
            current = s[i]
            if counter[current] < k:
                return max(self.divide_and_conquer(s, k, start , i - 1), self.divide_and_conquer(s, k, i + 1 , end))
            
        return end - start + 1

    def longestSubstring(self, s: str, k: int) -> int:
        if k == 1:
            return len(s)

        return self.divide_and_conquer(s, k, 0, len(s) - 1)

        
