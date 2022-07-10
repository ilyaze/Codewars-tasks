def fake_bin(x):
    a = []
    for i in x:
        if int(i) < 5:
            a.append('0')
        else:
            a.append('1')
    return ''.join(a)