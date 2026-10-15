import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    t = int(data[0])
    results = []
    idx = 1

    for _ in range(t):
        y = int(data[idx])
        x = int(data[idx + 1])
        idx += 2

        max_dim = max(y, x)
        direction = max_dim % 2

        start_range = (max_dim - 1) ** 2 + 1
        end_range = max_dim ** 2

        if direction == 0:
            if y < x:
                ans = start_range + (y - 1)
            else:
                ans = end_range - (x - 1)
        else:
            if y < x:
                ans = end_range - (y - 1)
            else:
                ans = start_range + (x - 1)

        results.append(str(ans))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()