"""
Problem : D2 1954 달팽이 숫자(Snail Number)

달팽이는 1 부터 N*N 까지의 숫자가 시계방향으로 이루어져 있다.
다음과 같이 정수 N을 입력 받아 N 크기의 달팽이를 출력하시오.

N이 3일 경우,
1 2 3
8 9 4
7 6 5

달팽이의 크기 N은 1 이상 10 이하의 정수이다.

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.

각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    """N x N 행렬을 1 부터 N*N 까지 달팽이 모양으로 출력한다.
    Extra explanation:
        N x N 행렬에서 달팽이 모양으로 행, 열을 이동해가며 1 부터 N*N 까지의 값을 저장한 뒤 출력한다.
        시계방향의 달팽이 모양이기 때문에 행, 열 이동은 우하좌상 순서로 이동한다.
    
    Variables:
        T : 테스트 케이스의 개수
        test_case : 테스트 케이스 리스트
        N : N x N 행렬의 크기
        result : 원소의 값이 1 부터 N*N 까지 달팽이 모양인 N x N 행렬
        drow : 행 이동 방향
        dcol : 열 이동 방향
        row : N x N 행렬의 행 번호
        col : N x N 행렬의 열 번호
        dindex : 행, 열 이동 방향
    
    Example:
        >>> 1       : input T
        >>> 3       : input test case N
        >>> #1      : output
        >>> 1 2 3
        >>> 8 9 4
        >>> 7 6 5
    """
    T = int(input())
    test_case = [int(input()) for t in range(T)]

    for t in range(1, T+1):
        N = test_case[t-1]

        if N == 1:
            print(f'#{t}')
            print(1)
            continue

        result = [([0] * N) for n in range(N)]
        drow = [0, 1, 0, -1]
        dcol = [1, 0, -1, 0]
        row = col = dindex = 0

        for n in range(1, N*N+1):
            result[row][col] = n
            nrow = row + drow[dindex]
            ncol = col + dcol[dindex]

            if nrow >= N or ncol >= N:
                dindex += 1
                if dindex > 3:
                    dindex = 0
                nrow = row + drow[dindex]
                ncol = col + dcol[dindex]

            if result[nrow][ncol] != 0:
                dindex += 1
                if dindex > 3:
                    dindex = 0
                    
            row += drow[dindex]
            col += dcol[dindex]

        print(f'#{t}')
        for row in range(N):
            for col in range(N):
                print(result[row][col], end=' ')
            print('')

solution()