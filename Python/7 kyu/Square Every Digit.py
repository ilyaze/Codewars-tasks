def square_digits(num):
    a = str(num)
    b = ''
    for i in a:
        c = int(i) ** 2
        b += str(c)
    return int(b)