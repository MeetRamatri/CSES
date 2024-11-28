def rep(s):
    max_length = 1
    current_length = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length

s = input()
print(rep(s))
