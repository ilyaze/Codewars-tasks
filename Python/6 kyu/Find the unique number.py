def find_uniq(arr):
    if arr[0] == arr[1]:
        a = arr[0]
    elif arr[1] == arr[2]:
        a = arr[1]
    elif arr[2] == arr[3]:
        a = arr[2]
    for i in arr:
        if i == a:
            continue
        else:
            return i
