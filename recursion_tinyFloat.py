import sys
sys.setrecursionlimit(2000)

def tinyFloat(a, half):
    half = a * half
    if half == 0.0:
        return a
    return tinyFloat(half, a)

print(tinyFloat(1.0, 0.5)) # what is the result, we can start with 1.0 and its half 0.5
