# Leetcode 832 - Flipping an Image

class Solution(object):
    def flipAndInvertImage(self, image):
        for row in image:
            row.reverse()
            for i in range(len(row)):
                row[i] ^= 1
        return image
