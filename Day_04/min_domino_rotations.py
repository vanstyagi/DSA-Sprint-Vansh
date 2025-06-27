# Leetcode 1007 - Minimum Domino Rotations For Equal Row

from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for x in [tops[0], bottoms[0]]:
            if all(x in pair for pair in zip(tops, bottoms)):
                return min(
                    len(tops) - tops.count(x),
                    len(bottoms) - bottoms.count(x)
                )
        return -1
