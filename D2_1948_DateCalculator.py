"""
Problem : D2 1948 날짜 계산기(Date Calculator)

월 일로 이루어진 날짜를 2개 입력 받아, 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력하는 프로그램을 작성하라.

월은 1 이상 12 이하의 정수이며, 각 달의 마지막 날짜는 다음과 같다.
1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31
두 번째 날짜가 첫 번째 날짜보다 항상 크게 주어진다.

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 4개의 수가 주어진다.
첫 번째 수가 월을 나타내고 두 번째 수가 일을 나타낸다. 그 다음 같은 형식으로 두 번째 날짜가 주어진다.

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    """월 일로 이루어진 두개의 날짜를 입력 받아 두 번째 날짜가 첫 번째 날짜의 며칠째인지 계산해 결과를 출력한다.

    Variables:
        T : 테스트 케이스의 개수
        test_case : 테스트 케이스 리스트
        month : 월별 일 수 리스트
        result : 두 번째 날짜가 첫 번째 날짜의 며칠째인지 계산한 결과값
        pre_month : 첫 번째 날짜의 월
        pre_day : 첫 번째 날짜의 일
        next_month : 두 번째 날짜의 월
        next_day : 두 번째 날짜의 일

    Example:
        >>> 1           : input T
        >>> 7 17 12 24  : input test case
        >>> #1 161      : output
    """
    T = int(input())
    test_case = [list(map(int, input().split())) for t in range(T)]
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for t in range(1, T+1):
        result = 0
        pre_month, pre_day, next_month, next_day = test_case[t-1][0], test_case[t-1][1], test_case[t-1][2], test_case[t-1][3]

        if next_month - pre_month > 0:
            for m in range(pre_month+1, next_month):
                result += month[m]
            result += month[pre_month] - pre_day + next_day + 1
        else:
            result = next_day - pre_day + 1
            
        print(f'#{t} {result}')

solution()