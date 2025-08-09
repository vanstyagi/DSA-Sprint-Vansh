def duplicateZeros(arr):  
    zeros = arr.count(0)  
    n = len(arr)  
    for i in range(n-1, -1, -1):  # Start from end  
        if i + zeros < n:  
            arr[i + zeros] = arr[i]  # Shift right  
        if arr[i] == 0:  
            zeros -= 1  
            if i + zeros < n:  
                arr[i + zeros] = 0  # Duplicate zero  