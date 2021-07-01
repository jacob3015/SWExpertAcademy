"""
Problem : D1 1545 거꾸로 출력해 보아요(Print Backwards)

주어진 숫자부터 0까지 순서대로 찍어보세요.

아래는 입력된 숫자가 N일 때 거꾸로 출력하는 예시입니다.
N, N-1, N-2, ..., 0
"""

def solution():
    # 주어진 숫자 N
    N = int(input())
    # N부터 0까지 출력
    for n in range(N, -1, -1):
        print(n, end=' ')

solution()