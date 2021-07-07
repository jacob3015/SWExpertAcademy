"""
Problem : D2 1984 중간 평균값 구하기(Calculate Average Except Max Min)

10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.
(소수점 첫째 자리에서 반올림한 정수를 출력한다.)

각 수는 0 이상 10,000 이하의 정수이다.

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    # 테스트 케이스의 개수 T
    T = int(input())

    # 테스트 케이스 test_case
    test_case = []

    # T번 반복하며, 각 테스트 케이스를 입력 받는다.
    for _ in range(T):
        test_case.append(list(map(int, input().split())))

    # T번 반복하며, 각 테스트 케이스의 결과를 출력한다.
    for t in range(1, T+1):
        # 하나의 테스트 케이스 array
        array = test_case[t-1]
        # 주어진 10개의 수 중 최대값과 최소값을 제외한 수들의 평균값 result
        result = round((sum(array) - max(array) - min(array))/8)
        # 결과를 출력한다.
        print(f'#{t} {result}')

solution()