"""
Problem : D1 2056 연월일 달력(Year-Month Calender)

연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면 ”YYYY/MM/DD”형식으로 출력하고,
날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.

연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
일은 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    # 테스트 케이스의 개수 T
    T = int(input())
    test_case = []
    # T번 반복하며, 테스트 케이스를 입력 받는다.
    for _ in range(T):
        test_case.append(input())
    # T번 반복하며, 테스트 케이스의 날짜가 유효한지 확인한 뒤 결과를 출력한다.
    for t in range(1, T+1):
        year, month, day = test_case[t-1][:4], test_case[t-1][4:6], test_case[t-1][6:8]
        result = False
        
        if int(month) == 2:
            if 0 < int(day) < 29:
                result = True
        elif 0 < int(month) < 8:
            if int(month) % 2 == 1 and 0 < int(day) < 32:
                result = True
            elif int(month) % 2 == 0 and 0 < int(day) < 31:
                result = True
        elif 7 < int(month) < 13:
            if int(month) % 2 == 1 and 0 < int(day) < 31:
                result = True
            elif int(month) % 2 == 0 and 0 < int(day) < 32:
                result = True

        if result:
            print(f"#{t} {year}/{month}/{day}")
        else:
            print(f"#{t} -1")

solution()