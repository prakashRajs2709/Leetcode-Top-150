class Solution:
    def containsNearbyDuplicate(self, n: List[int], k: int) -> bool:
        d = {}
        for i, num in enumerate(n):
            if num in d and i - d[num] <= k:
                return True
            d[num] = i
        return False



