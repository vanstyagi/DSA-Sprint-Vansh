def shortestPalindrome(s):
    t = s + "#" + s[::-1]
    lps = [0] * len(t)
    
    for i in range(1, len(t)):
        j = lps[i - 1]
        while j > 0 and t[i] != t[j]:
            j = lps[j - 1]
        if t[i] == t[j]:
            j += 1
        lps[i] = j
    longest_palindrome_prefix = lps[-1]
    suffix = s[longest_palindrome_prefix:]
    
    return suffix[::-1] + s