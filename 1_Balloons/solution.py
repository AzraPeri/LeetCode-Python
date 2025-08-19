# Problem: Maximum Number of Balloons
# Link: https://leetcode.com/problems/maximum-number-of-balloons/

from collections import Counter

def maxNumberOfBalloons(text: str) -> int:
    counts = Counter(text)
    needed = Counter("balloon")
    result = float('inf')
    for ch in needed:
        result = min(result, counts.get(ch, 0) // needed[ch])
    return result

# Test
print(maxNumberOfBalloons("nlaebolko"))  # Output: 1
