# Leetcode 164 - Maximum Gap (Bucket Sort)

class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0

        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0

        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1

        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets[idx][0] = min(num, buckets[idx][0])
            buckets[idx][1] = max(num, buckets[idx][1])

        max_gap = 0
        prev_max = min_val

        for b in buckets:
            if b[0] == float('inf'):
                continue
            max_gap = max(max_gap, b[0] - prev_max)
            prev_max = b[1]

        return max_gap
