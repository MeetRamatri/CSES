n=int(input())
lis=list(map(int,input().split()))
s=(n*(n+1))//2
print(s-sum(lis))