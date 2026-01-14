def reverseWords(s):
    s = list(s)
    n = len(s)

    def reverse(l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    
    def reverse_each_word():
        start = end = 0
        while start < n:

            while start < n and s[start] == ' ':
                start += 1

            end = start
            while end < n and s[end] != ' ':
                end += 1

            reverse(start, end - 1)
            start = end

    def clean_spaces():
        i = j = 0
        while j < n:
            while j < n and s[j] == ' ':
                j += 1
            while j < n and s[j] != ' ':
                s[i] = s[j]
                i += 1
                j += 1
            while j < n and s[j] == ' ':
                j += 1
            if j < n:
                s[i] = ' '
                i += 1

        return i
    
    reverse(0, n - 1)
    reverse_each_word()
    new_len = clean_spaces()
    
    return ''.join(s[:new_len])