def topKFrequent(words, k):
    from collections import Counter

    freq = Counter(words)
    unique_words = list(freq.keys())
    unique_words.sort(key=lambda word: (-freq[word], word))
    return unique_words[:k]
