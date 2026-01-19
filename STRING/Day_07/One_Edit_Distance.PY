def isOneEditDistance(s, t):
    def are_equal(str1, str2):
        return str1 == str2
    if abs(len(s) - len(t)) > 1:
        return False
    if len(s) > len(t):
        for i in range(len(s)):

            if are_equal(s[:i] + s[i+1:], t):
                return True
    elif len(t) > len(s):
        for i in range(len(t)):
            if are_equal(t[:i] + t[i+1:], s):
                return True
    else:  
        for i in range(len(s)):
            if s[i] != t[i]:
                if are_equal(s[:i] + t[i] + s[i+1:], t):
                    return True
        return False

    return False