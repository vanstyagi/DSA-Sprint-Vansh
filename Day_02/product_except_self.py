def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n
    
    # Left Pass: Compute prefix products
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]
    
    # Right Pass: Compute suffix products and merge
    right_product = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]
    
    return answer