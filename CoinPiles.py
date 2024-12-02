t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if (a + b) % 3 != 0:
         print("NO")
    elif a > 2 * b or b > 2 * a:
        print("NO") 
    else:
        print("YES")
