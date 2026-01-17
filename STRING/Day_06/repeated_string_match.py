def repeatedStringMatch(a, b):
    min_reps = (len(b) + len(a) - 1) // len(a)  
    
    for reps in [min_reps, min_reps + 1]:
        repeated = a * reps
        if b in repeated:
            return reps
    return -1