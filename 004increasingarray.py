n = int(input())
list = [int(i) for i in input().split()]

count = 0

for i in range(1, n):
    if list[i-1] > list[i]:
        count += list[i-1] - list[i]
        list[i] = list[i-1]

print(count)