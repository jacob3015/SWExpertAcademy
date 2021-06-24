"""
Problem : D1 2070 큰 놈, 작은 놈, 같은 놈(Big, Little, Same)

2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.

각 수는 0 이상 10000 이하의 정수이다.

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    # 테스트 케이스의 개수 T
    T = int(input())
    # 테스트 케이스를 저장할 test_case
    test_case = []
    # T번 반복하며, 각 테스트 케이스를 입력 받아 비교한 결과를 저장한다.
    for _ in range(T):
        a, b = map(int, input().split())
        result = ""
        if a > b : result = ">"
        elif a < b : result = "<"
        else : result = "="
        test_case.append(result)
    # T번 반복하며, 각 테스트 케이스의 비교 결과를 출력한다.
    for t in range(1, T+1):
        print(f"#{t} {test_case[t-1]}")

solution()