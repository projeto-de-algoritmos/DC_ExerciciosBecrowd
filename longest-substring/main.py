from collections import Counter


def divide_and_conquer(
    s: str, 
    k: int, 
    start: int, 
    end: int
) -> int:
    if start == end:
        return 0

    counter = Counter()

    for i in range(start, end + 1):
        counter[s[i]] += 1

    for i in range(start, end + 1):
        current = s[i]
        if counter[current] < k:
            return max(divide_and_conquer(s, k, start , i - 1), divide_and_conquer(s, k, i + 1 , end))
        
    return end - start + 1


def longest_substring(
    s: str, 
    k: int
) -> int:
    if k == 1:
        return len(s)

    return divide_and_conquer(s, k, 0, len(s) - 1)

    
if __name__ == "__main__":
    s = "aaabb"
    k = 3
    print(longest_substring(s, k))
