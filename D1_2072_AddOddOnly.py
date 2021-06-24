"""
Problem : D1 2072 홀수만 더하기(Add Odd Only)

10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

각 수는 0이상 10,000 이하의 정수이다.

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 텍스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

출력은 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    # 테스트 케이스의 개수 T
    T  = int(input())
    # 테스트 케이스 test_case
    test_case = []
    # T번 반복하며, 테스트 케이스를 입력 받아 test_case에 저장한다.
    for _ in range(T):
        test_case.append(list(map(int, input().split())))
    # T번 반복하며, 각 테스트 케이스 10개의 수 중 홀수만을 더해 결과를 출력한다.
    for t in range(1, T+1):
        result = 0
        for num in test_case[t-1]:
            if num % 2 == 1:
                result += num
        print(f"#{t} {result}")

solution()