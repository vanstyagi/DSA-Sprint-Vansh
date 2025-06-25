def findMaxConsecutiveOnes(nums):
    max_streak = current_streak = 0
    for num in nums:
        if num == 1:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0  # Reset streak
    return max_streak