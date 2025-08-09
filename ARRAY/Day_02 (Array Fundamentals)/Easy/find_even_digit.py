def findNumbers(nums):
    count = 0
    for num in nums:
        digits = 0
        n = abs(num)  # Handle negatives
        if n == 0:
            digits = 1
        else:
            while n > 0:
                digits += 1
                n = n // 10
        if digits % 2 == 0:
            count += 1
    return count