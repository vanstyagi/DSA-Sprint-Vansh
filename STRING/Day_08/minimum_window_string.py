def minWindow(s, t):
    from collections import Counter

    t_count = Counter(t)
    n = len(s)
    min_window = ""

    for i in range(n):
        window_count = Counter()
        needed = len(t_count)  
        satisfied = 0

        for j in range(i, n):
            char = s[j]
            window_count[char] += 1
            if char in t_count and window_count[char] == t_count[char]:
                satisfied += 1
            if satisfied == needed:
                if not min_window or (j - i + 1) < len(min_window):
                    min_window = s[i:j+1]
                break 

    return min_window
