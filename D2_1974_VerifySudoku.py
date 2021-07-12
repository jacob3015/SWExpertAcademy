"""
Problem : D2 1974 스도쿠 검증(Verify Sudoku)

스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.
같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자라 겹치지 않아야 한다.
입력으로 9 x 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.

퍼즐은 모두 숫자로 채워진 상태로 주어진다.
입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.

테스트 케이스 t에 대한 결과는 '#t'을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    """9 x 9 크기의 스도쿠를 입력 받아 정답 결과를 출력한다.
    원소의 중복을 허용하지 않는 set 자료형을 이용해 스도쿠의 각 행, 열, 3 x 3 격자의 원소 개수가 9개를 만족하는지 비교한다.
    set 자료형으로 변환한 스도쿠의 각 행, 열, 격자의 원소 개수가 9개면 결과로 1을, 아니면 0을 출력한다.


    Variables:
        T : 테스트 케이스의 개수
        test_case : 주어진 테스트 케이스 리스트
        sudoku : 각 테스트 케이스 별 주어진 9 x 9 크기의 스도쿠
        result : 스도쿠의 정답 결과, 정답이면 True, 오답이면 False
        row : 스도쿠의 행(line:61, 62), 스도쿠의 행 번호
        col : 스도쿠의 열 번호
        line : 스도쿠의 열
        start_row : 스도쿠의 3 x 3 격자 좌상단의 행 번호
        start_col : 스도쿠의 3 x 3 격자 좌상단의 열 번호
        grid : 스도쿠의 3 x 3 격자

    Example:
        >>> 1                   : input T
        >>> 7 3 6 4 2 9 5 8 1   : input sudoku row 1
        >>> 5 8 9 1 6 7 3 2 4   : input sudoku row 2
        >>> 2 1 4 5 8 3 6 9 7   : input sudoku row 3
        >>> 8 4 7 9 3 6 1 5 2   : input sudoku row 4
        >>> 1 5 3 8 4 2 9 7 6   : input sudoku row 5
        >>> 9 6 2 7 5 1 8 4 3   : input sudoku row 6
        >>> 4 2 1 3 9 8 7 6 5   : input sudoku row 7
        >>> 3 9 5 6 7 4 2 1 8   : input sudoku row 8
        >>> 6 7 8 2 1 5 4 3 9   : input sudoku row 9
        >>> #1 1                : output
    """
    T = int(input())
    test_case = []
    for _ in range(T):
        sudoku = [list(map(int, input().split())) for line in range(9)]
        test_case.append(sudoku)

    for t in range(1, T+1):
        sudoku = test_case[t-1]

        result = True
        
        for row in sudoku:
            result = len(set(row)) == 9
            if not result:
                break
        
        if result:
            for col in range(9):
                line = []
                for row in range(9):
                    line.append(sudoku[row][col])
                result = len(set(line)) == 9
                if not result:
                    break
        
        if result:
            for start_row in range(0, 9, 3):
                for start_col in range(0, 9, 3):
                    grid = []
                    for row in range(start_row, start_row+3):
                        for col in range(start_col, start_col+3):
                            grid.append(sudoku[row][col])
                    result = len(set(grid)) == 9
                    if not result:
                        break
                if not result:
                    break

        if result:
            print(f'#{t} 1')
        else:
            print(f'#{t} 0')

solution()