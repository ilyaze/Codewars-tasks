def narcissistic(value):
    arr = []
    arr1 = []
    for values in str(value):
        arr.append(int(values))
    for arrs in arr:
        arr1.append(arrs ** len(str(value)))
    if value == sum(arr1):
        return True
    else:
        return False