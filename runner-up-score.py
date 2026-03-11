if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    for x in arr:
        if x > max_v:
            max_v = x
    while max_v in arr:
        arr.remove(max_v)
    score = arr[0]
    for y in arr:
        if y > score:
            score = y
    print(score)
