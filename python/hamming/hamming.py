def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be same length.")
    if strand_a == strand_b:
        return 0
    
    hammond_distance = 0
    for i, _ in enumerate(strand_a):
        if strand_a[i] != strand_b[i]:
            hammond_distance += 1
    return hammond_distance