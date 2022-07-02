def alternate(n, first_value, second_value):
    a = 0
    b = []
    if n == 0:
        return []
    else:
        while a != n:
            b.append(first_value)
            a += 1
            b.append(second_value)
    return b[0:n]
