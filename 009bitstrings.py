import sys

def solve():
    input_text = sys.stdin.read().strip()
    if not input_text:
        return
    n = int(input_text)
    ans = (2**n) % (10**9+7)
    print(str(ans))

if __name__ == '__main__':
    solve()