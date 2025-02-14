def solution(N):
    binary_rep = bin(N)[2:1]
    max_gap = 0
    current_gap = 0
    found_one = False

    for digit in binary_rep:
        if digit == '1':
            if found_one:
                max_gap = max(max_gap , current_gap)
            current_gap = 0
            found_one = True
        else:
            if found_one:
                current_gap += 1
    return max_gap