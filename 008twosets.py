import sys
import math

def solve():
    input_text = sys.stdin.read().strip()
    if not input_text:
        return
    n = int(input_text)
    
    total_sum = 0.5 * n * (n+1)

    if total_sum % 2 != 0:
        print("NO")
        return

    else:
        a = [n]
        b = []
        sum_a = n
        sum_b = 0

        for i in range(n-1, 0, -1):
            if sum_b <= sum_a:
                b.append(i)
                sum_b += i
            else:
                a.append(i)
                sum_a += i

        out = ["YES", str(len(a)), " ".join(map(str, a)), str(len(b)), " ".join(map(str, b))]

        sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()