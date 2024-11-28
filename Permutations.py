def beautiful_permutation(n):
    if n == 1:
        return [1]
    elif n < 4:
        return -1
    else:
        even_numbers = list(range(2, n+1, 2))
        odd_numbers = list(range(1, n+1, 2))
        return even_numbers + odd_numbers

n = int(input())
result = beautiful_permutation(n)
if result == -1:
    print("NO SOLUTION")
else:
    print(" ".join(map(str, result)))
