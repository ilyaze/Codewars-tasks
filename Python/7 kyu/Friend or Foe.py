def friend(x):
    a = []
    for i in x:
        if len(i) == 4:
            a.append(i)
        else:
            continue
    return a