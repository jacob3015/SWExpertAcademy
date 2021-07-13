"""
Problem : D2 1961 숫자 배열 회전(Matrix Rotation)

N x N 행렬이 주어질 때, 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.
N은 3 이상 7 이하이다.

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N이 주어지고, 다음 N 줄에는 N x N 행렬이 주어진다.

출력의 첫 줄은 '#t'로 시작하고, 다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    """주어진 N x N 행렬을 시계방향으로 90도, 180도, 270도 회전한 모양을 출력한다.
    Extra explanation:
        주어진 행렬을 회전시키지 않고 시계 방향으로 90도, 180도, 270도로 회전한 모양에 맞게 읽은 결과를 출력한다.
    
    Variables:
        T : 테스트 케이스의 개수
        test_case : 주어진 테스트 케이스 리스트
        N : 행렬의 크기
        matrix : 주어진 N x N 행렬
        result : 주어진 행렬을 시계 방향으로 90도(결과 행렬의 첫번째 열), 180도(결과 행렬의 두번째 열), 270도(결과 행렬의 세번째 열)로 회전한 모양의 결과
        result_row : 결과 행렬의 행 번호
        result_col : 결과 행렬의 열 번호
        row : matrix의 행 번호
        col : matrix의 열 번호

    Example:
        >>> 1           : input T
        >>> 3           : input N
        >>> 1 2 3       : input test case matrix row 1
        >>> 4 5 6       : input test case matrix row 2
        >>> 7 8 9       : input test case matrix row 3
        >>> 741 987 369 : output result matrix row 1
        >>> 852 654 258 : output result matrix row 2
        >>> 963 321 147 : output result matrix row 3
    """
    T = int(input())
    test_case = []

    for _ in range(T):
        N = int(input())
        matrix = [list(map(int, input().split())) for n in range(N)]
        test_case.append(matrix)

    for t in range(1, T+1):
        matrix = test_case[t-1]
        N = len(matrix)

        result = [(['']*3) for n in range(N)]

        result_row = result_col = 0
        for col in range(N):
            for row in range(N-1, -1, -1):
                result[result_row][result_col] += str(matrix[row][col])
            result_row += 1

        result_row, result_col = 0, 1
        for row in range(N-1, -1, -1):
            for col in range(N-1, -1, -1):
                result[result_row][result_col] += str(matrix[row][col])
            result_row += 1
        
        result_row, result_col = 0, 2
        for col in range(N-1, -1, -1):
            for row in range(N):
                result[result_row][result_col] += str(matrix[row][col])
            result_row += 1
        
        print(f'#{t}')
        for row in range(N):
            for col in range(3):
                print(result[row][col], end=' ')
            print('')

solution()