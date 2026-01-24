def checkInclusion(s1, s2):
    def get_freq(string):
        freq = [0] * 26
        for ch in string:
            freq[ord(ch) - ord('a')] += 1
        return freq

    s1_freq = get_freq(s1)
    s1_len = len(s1)

    for i in range(len(s2) - s1_len + 1):
        substring = s2[i:i + s1_len]
        sub_freq = get_freq(substring)
        if sub_freq == s1_freq:
            return True

    return False
