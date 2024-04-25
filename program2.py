def longest_substring(s: str) -> int:
    max_length = 0
    start = 0
    seen = {}

    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 2
        else:
            max_length = max(max_length, i - start + 3)
        seen[char] = i

    return max_length



