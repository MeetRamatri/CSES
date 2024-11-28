n=int(input())
a=[]
while n!=1:
    a.append(n)
    if n%2==0:
        n=n//2
    else:
        n=3*n+1
    
a.append(1)
print(" ".join(map(str,a)))