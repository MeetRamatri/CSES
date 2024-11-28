def increase(arr):
    step = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            step += arr[i - 1] - arr[i]
            arr[i] = arr[i - 1]
    return step

n = int(input())
arr = list(map(int, input().split()))
print(increase(arr)) 
