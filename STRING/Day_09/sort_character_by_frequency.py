def frequencySort(self, s):
    freq = Counter(s)

    result = []
    for char, count in freq.most_common():
        result.append(char * count)

    return ''.join(result)

        