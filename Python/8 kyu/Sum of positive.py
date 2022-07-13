def positive_sum(arr):
    a = 0
    for i in arr:
        if i >= 0:
            a += i
        else:
            continue
    return a