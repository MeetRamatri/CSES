n = int(input())
sum = n * (n + 1) // 2
if sum % 2 != 0:
    print("NO")
else:
    print("YES")
    set1 = []
    set2 = []
    half_sum = sum // 2
    current_sum = 0
    for i in range(n, 0, -1):
        if current_sum + i <= half_sum:
            set1.append(i)
            current_sum += i
        else:
            set2.append(i)
    print(len(set1))
    print(" ".join(map(str, set1)))
    print(len(set2))
    print(" ".join(map(str, set2)))
