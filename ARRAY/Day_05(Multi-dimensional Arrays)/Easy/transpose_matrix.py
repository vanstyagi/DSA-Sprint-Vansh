class Solution(object):
    def transpose(self, matrix):
        return zip(*matrix) if not matrix else [list(row) for row in zip(*matrix)]
