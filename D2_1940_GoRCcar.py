"""Problem : D2 1940 가랏!RC카!(Go! RC car!)
RC카의 이동거리를 계산하려고 한다.
입력으로 매초마다 아래와 같은 command가 정수로 주어진다.
0 : 현재 속도 유지, 1 : 가속, 2 : 감속
위 command 중, 가속 또는 감속의 경우 가속도의 값이 추가로 주어진다.
가속도의 단위는 m/s^2 이며, 모두 양의 정수로 주어진다.
입력으로 주어진 N 개의 command를 모두 수행했을 때, N 초 동안 이동한 거리를 계산하는 프로그램을 작성하라.
RC 카의 초기 속도는 0m/s 이다.

N은 2 이상 30 이하의 정수이다.
가속도의 값은 1m/s^2 또는 2m/s^2 이다.
현재 속도보다 감속할 속도가 더 클 경우, 속도는 0m/s 가 된다.

입력은 첫 줄에 총 테스트 케이스의 개수 T, 다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스 첫 줄에는 command의 수 N이 주어지고, 둘째 줄부터 매 줄마다 각각의 command가 주어진다.

테스트 케이스 t에 대한 결과는 '#t'을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    """주어진 command를 입력 받아 RC카가 이동한 거리를 구해 출력한다.

    Variables:
        T : 테스트 케이스의 개수
        test_case : 주어진 테스트 케이스 리스트
        N : 하나의 테스트 케이스에서 command의 개수
        commands : 주어진 command 리스트
        result : RC카가 이동한 거리
        velocuty : RC카의 속도
        acceleration : RC카의 가속도
    
    Example:
        >>> 1       : input T
        >>> 2       : input N
        >>> 1 2     : input commands
        >>> 2 1
        >>> #1 3    : output result
    """
    T = int(input())
    test_case = []

    for _ in range(T):
        N = int(input())
        commands = [list(map(int, input().split())) for _ in range(N)]
        test_case.append(commands)

    for t in range(1, T+1):
        commands = test_case[t-1]
        result = velocity = 0

        for com in commands:
            if len(com) > 1:
                acceleration = com[1]
                if com[0] == 2:
                    acceleration *= (-1)
                velocity += acceleration
                if velocity < 0:
                    velocity = 0
            result += velocity

        print(f'#{t} {result}')

solution()