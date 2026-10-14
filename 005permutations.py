n = int(input())

if n == 1:
    print(n)
elif n <= 3:
    print("NO SOLUTION")
elif n == 4:
    print("3 1 4 2")

else:
    for i in range(1, n+1, 2):
        print(str(i))
    for i in range(2, n+1, 2):
        print(str(i))

