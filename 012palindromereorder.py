import sys
from collections import defaultdict

def solve():
    input_text = sys.stdin.read().strip()
    if not input_text:
        return
    
    n = len(input_text)
    
    char_count = defaultdict(int)
    
    for char in input_text:
        char_count[char] += 1

    # two cases: all even counts or one odd count with rest even counts.

    odd_count = 0

    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    if odd_count > 1:
        print("NO SOLUTION")
        return
    
    res = [""] * n

    l, r = 0, n-1
        
    for char, count in char_count.items():
        for _ in range(count // 2): 
            res[l] = char
            res[r] = char
            l += 1
            r -= 1
        if count % 2 == 1:   
            res[n // 2] = char
    
    print("".join(res))
    

if __name__ == '__main__':
    solve()