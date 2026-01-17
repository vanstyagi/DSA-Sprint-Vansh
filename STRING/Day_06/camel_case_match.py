def camelMatch(self, queries, pattern):
        def is_match(query, pattern):
            pattern_idx = 0
            n = len(pattern)
    
            for char in query:
                if pattern_idx < n and char == pattern[pattern_idx]:
                    pattern_idx += 1
                elif char.isupper():
                    return False
    
            return pattern_idx == n
        return [is_match(q, pattern) for q in queries]

        