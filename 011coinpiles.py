import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    t = int(data[0])
    results = []
    idx = 1

    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2

        if (a+b) % 3 != 0 or (a * 2 < b) or (b * 2 < a):
            results.append("NO")
        else:
            results.append("YES")

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()