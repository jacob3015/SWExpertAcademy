"""
Problem : D1 2019 더블더블(Double Double)

1부터 주어진 횟수까지 2를 곱한 값들을 출력하시오.
주어질 숫자는 30을 넘지 않는다.
"""

def solution():
    # 주어진 횟수 N
    N = int(input())
    # 주어진 횟수 만큼 2를 곱한 값들을 출력한다.
    for t in range(N+1):
        print(2**t, end=' ')

solution()