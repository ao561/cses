import sys
import math
 
def solve():
    input_text = sys.stdin.read().strip()
    if not input_text:
        return
    n = int(input_text)
 
    trailing_zeros = 0
 
    while n >= 5:
        n //= 5
        trailing_zeros += n
 
    print(str(trailing_zeros))
 
if __name__ == '__main__':
    solve()