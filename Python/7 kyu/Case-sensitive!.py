def case_sensitive(s):
    arr = []
    if s == s.lower():
        return [True, []]
    else:
        for i in s:
            if i == i.upper():
                arr.append(i)
            else:
                continue
        return [False, arr]