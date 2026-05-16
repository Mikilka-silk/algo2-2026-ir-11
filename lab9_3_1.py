def _build_transition_table(needle):    
    m = len(needle)
    tf = [{} for _ in range(m + 1)]
    unique_chars = set(needle)

    for state in range(m + 1):
        for char in unique_chars:
            next_state = min(m + 1, state + 2)
            while next_state > 0:
                next_state -= 1
                if (needle[:state] + char).endswith(needle[:next_state]):
                    tf[state][char] = next_state
                    break
    return tf
    
def search_finite(haystack, needle):
    if not needle or not haystack:
        return []
    
    m = len(needle)
    n = len(haystack)
    tf = _build_transition_table(needle)

    current_state = 0
    indices = []

    for i in range(n):
        current_state = tf[current_state].get(haystack[i], 0)

        if current_state == m:
            indices.append(i - m + 1)

    return indices