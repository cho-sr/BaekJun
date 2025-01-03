import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    H,W,N = map(int,input().split())

    A = 1
    B = 1
    cnt = 1
    for j in range(W):
        for k in range(H):
            if A > H:
                A = 1
            if cnt == N:
                print(A*100 + B)
            A = A + 1
            cnt = cnt + 1
        B = B + 1