n = int(input())
list = [int(i) for i in input().split()]

print(str(int(0.5*n*(n+1) - sum(list))))