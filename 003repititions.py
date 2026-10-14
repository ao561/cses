s = input()

n = len(s)
l = 0
max_length = 0

for r in range(n):
    if s[r] != s[l]:
        l = r
    max_length = max(max_length, r-l+1)


print(max_length)
