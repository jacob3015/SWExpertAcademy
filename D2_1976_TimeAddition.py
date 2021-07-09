"""
Problem : D2 1976 시각 덧셈(Time Addition)

시 분으로 이루어진 시작을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.
(시각은 12시간제로 표시한다. 즉, 시가 가질 수 있는 값은 1시부터 12시이다.)

시는 1 이상 12 이하의 정수이다. 분은 0 이상 59 이하의 정수이다.

입력 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫번째 줄에는 4개의 수가 주어진다.
첫 번째 수가 시를 나타내고 두 번째 수가 분을 나타낸다. 그 다음 같은 형식으로 두 번째 시각이 주어진다.

출력의 각 줄은 '#t'로 시작하고 공백을 한 칸 둔 다음, 시를 출력하고 공백을 한 칸 둔 다음 분을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    """두 개의 시각을 입력 받아 더한 결과를 출력한다.

    Variables:
        T : 테스트 케이스의 개수
        test_case : 주어진 테스트 케이스 리스트
        hour : 주어진 시각에서 시의 합
        minute : 주어진 시각에서 분의 합
    
    Example:
        >>> 1           : input T
        >>> 3 17 1 39   : input test case
        >>> # 1 4 56    : output
    """
    T = int(input())
    test_case = [list(map(int, input().split())) for t in range(T)]
    
    for t in range(1, T+1):
        hour = test_case[t-1][0] + test_case[t-1][2]
        minute = test_case[t-1][1] + test_case[t-1][3]

        if minute > 59:
            hour += 1
            minute -= 60
        if hour > 12:
            hour -= 12

        print(f'#{t} {hour} {minute}')

solution()