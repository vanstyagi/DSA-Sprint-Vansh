def spiralOrder(matrix):
    if not matrix: return []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    res = []
    
    while top <= bottom and left <= right:
        # Right
        res += matrix[top][left:right + 1]
        top += 1
        
        # Down
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # Left
            res += matrix[bottom][left:right + 1][::-1]
            bottom -= 1
        
        if left <= right:
            # Up
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
    return res