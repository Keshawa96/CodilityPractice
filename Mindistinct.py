from collections import Counter

def solution(A, K):
    freq = Counter(A)  # Count occurrences of each number
    sorted_freq = sorted(freq.items(), key=lambda x: x[1])  # Sort by frequency (low to high)
    
    distinct_count = len(sorted_freq)  # Initial distinct elements count
    
    for num, count in sorted_freq:
        if K >= count:
            K -= count
            distinct_count -= 1  # Reduce distinct count
        else:
            break  # Stop if we can't remove an entire group

    return distinct_count