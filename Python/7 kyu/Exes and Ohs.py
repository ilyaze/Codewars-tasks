def xo(s):
    countx, counto = 0, 0
    for i in s:
        if i == 'x' or i == 'X':
            countx += 1
        elif i == 'o' or i == 'O':
            counto += 1
    return countx == counto