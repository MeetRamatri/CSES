def gray_code(n):
    if n == 0:
        return ["0"]
    elif n == 1:
        return ["0", "1"]
    else:
        previous_gray_code = gray_code(n - 1)
        result = []
        for code in previous_gray_code:
            result.append("0" + code)
        for code in reversed(previous_gray_code):
            result.append("1" + code)
        return result

n = int(input())
gray_codes = gray_code(n)
for code in gray_codes:
    print(code)
