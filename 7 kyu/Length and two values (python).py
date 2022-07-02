def alternate(n, first_value, second_value):
    a, b = [], 0
    while b != n:
        a.append(first_value); a.append(second_value); b += 1
    return a[0:n]
