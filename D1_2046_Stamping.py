"""
Problem : D1 2046 스탬프 찍기(Stamping)

주어진 숫자만큼 # 을 출력해보세요.

주어질 숫자는 100,000 이하다.
"""

def solution():
    # 주어진 숫자 N
    N = int(input())
    # N번 반복하며, '#'을 출력한다.
    for _ in range(N):
        print('#', end='')

solution()