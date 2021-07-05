"""
Problem : D2 2001 파리 퇴치(Defeat Flies)

N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라.
예를 들어 M = 2 일 경우 위 예제의 정답은 49마리가 된다.

1. N 은 5 이상 15 이하이다.
2. M 은 2 이상 N 이하이다.
3. 각 영역의 파리 갯수는 30 이하 이다.

가장 첫 줄에는 테스트 캐이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
다음 N 줄에 걸쳐 N x N 배열이 주어진다.

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하여 1부터 시작한다.)
"""


def solution():
    # 테스트 케이스의 개수 T
    T = int(input())

    # 테스트 케이스 test_case
    test_case = []

    # T번 반복하며, 각 테스트 케이스를 입력 받고 결과를 구한다.
    for _ in range(T):

        # 배열의 크기 N, 파리채의 크기 M
        N, M = map(int, input().split())
        # 배열 array
        array = []
        # N x N 배열을 입력 받는다.
        for _ in range(N):
            array.append(list(map(int, input().split())))
        
        # 죽은 파리의 개수 flies
        flies = []
        # 배열을 탐색하며 파리채로 죽은 파리 개수를 구한다.
        for row in range(N-M+1):
            for col in range(N-M+1):
                result = 0
                for nrow in range(M):
                    for ncol in range(M):
                        result += array[row+nrow][col+ncol]
                flies.append(result)

        """
        Worst case(N 이 최대, M 이 최소일 때)
        시간복잡도 : O(N**2) (T < N)
        N 이 최대이며, M 이 최소일 때 반복 횟수가 가장 많다.
        따라서 M 이 2일 때로 시간복잡도를 계산하면 T(N-1)**2 이다.
        이 때, T가 N보다 작다고 한다면 시간복잡도는 O(N**2) 이라고 할 수 있다.
        """
        
        # 파리채로 죽은 파리 개수 중 최댓값을 test_case에 저장한다.
        test_case.append(max(flies))

    # T번 반복하며, 결과를 출력한다.
    for t in range(1, T+1):
        print(f'#{t} {test_case[t-1]}')

solution()