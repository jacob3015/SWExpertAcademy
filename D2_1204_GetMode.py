"""Problem : D2 1204 최빈수 구하기(Get Mode)

어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.
이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 여기서 최빈수를 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.
최빈수를 출력하는 프로그램을 작성하여라.
(단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라.)

학생의 수는 1000명이며, 각 학생의 점수를 0점 이상 100점 이하의 값이다.

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄부터는 점수가 주어진다.

#부호와 함께 테스트 케이스의 번호를 출력하고, 한 칸 띄고, 테스트 케이스에 대한 답을 출력한다.
"""

def solution():
    """주어진 점수들의 최빈수를 구해 출력한다.
    Extra explanation:
        Counter sort를 활용해 주어진 점수들 중 최빈수(mode)를 구한다.
    
    Variables:
        T : 테스트 케이스의 개수
        test_case : 주어진 테스트 케이스 list
        test_case_number : 테스트 케이스 번호
        scores : 학생들의 점수 list
        count_socre : 학생들 점수의 등장 횟수를 세기 위한 list(Counter sort를 위한 list)
        mode : 학생들 점수 중 최빈수

    Example:
        >>> 1                       : input T
        >>> 1                       : input test case number
        >>> 96 98 72 ... 92 56 45   : input students score
        >>> #1 71                   : output mode
    """
    T = int(input())
    test_case = []

    for _ in range(T):
        test_case_number = input()
        test_case.append(list(map(int, input().split())))

    for t in range(1, T+1):
        scores = test_case[t-1]
        count_score = [0 for _ in range(101)]

        for s in scores:
            count_score[s] += 1
        mode = max(count_score)

        for s in range(100, -1, -1):
            if count_score[s] == mode:
                print(f'#{t} {s}')
                break

solution()