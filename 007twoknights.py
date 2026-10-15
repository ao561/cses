import sys
import math

def solve():
    input_text = sys.stdin.read().strip()
    if not input_text:
        return
    n = int(input_text)
    
    out = []
    
    for k in range(1, n + 1):
        total_comb = math.comb(k**2, 2) - 4 * (k-1) * (k-2)

        out.append(str(total_comb))
        
    
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()