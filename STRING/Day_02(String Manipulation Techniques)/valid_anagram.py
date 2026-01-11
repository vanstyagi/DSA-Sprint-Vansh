def isAnagram(s, t):
    if len(s) != len(t):
        return False
    char_count = [0] * 26

    for char in s:
        char_count[ord(char) - ord('a')] += 1

    for char in t:
        char_count[ord(char) - ord('a')] -= 1
        if char_count[ord(char) - ord('a')] < 0:
            return False

    return all(count == 0 for count in char_count)