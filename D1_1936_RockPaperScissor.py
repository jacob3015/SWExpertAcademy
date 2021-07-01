"""
Problem : D1 1936 가위바위보(Rock Paper Scissor)

A와 B가 가위바위보를 하였다.
가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.
A와 B 중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.

입력으로 A와 B가 무엇을 냈는지 빈 칸을 사이로 주어진다.

A가 이기면 A, B가 이기면 B를 출력한다.
"""

def solution():
    # A, B 입력 받기
    A, B = map(int, input().split())
    # A가 이기는 경우, 'A' 출력
    if (A, B) == (1, 3) or (A, B) == (2, 1) or (A, B) == (3, 2):
        print('A')
    # B가 이기는 경우, 'B' 출력
    else:
        print('B')

solution()