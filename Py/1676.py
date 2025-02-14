import sys
import math
input = sys.stdin.readline
n = int(input())
def Factorial():
    return math.factorial(n)
F = Factorial()
cnt = 0
while n >= 5:
    cnt += n // 5
    n = n // 5
print(cnt)





