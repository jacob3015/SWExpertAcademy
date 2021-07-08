"""
Problem : D2 1979 어디에 단어가 들어갈 수 있을까(Word Puzzle)

N x N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

1. N은 5 이상 15 이하의 정수이다.
2. K는 2 이상 N 이하의 정수이다.

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K가 주어진다.
테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.

테스트 케이스 t에 대한 결과를 '#t"을 찍고, 한 칸 띄고 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    # 테스트 케이스를 입력 받는다.
    T = int(input())
    test_case = []
    for _ in range(T):
        N, K = map(int, input().split())
        puzzle = []
        for _ in range(N):
            puzzle.append(list(map(int, input().split())))
        puzzle.append((N, K))
        test_case.append(puzzle)
    
    # 주어진 테스트 케이스 결과를 출력한다.
    for t in range(1, T+1):
        puzzle = test_case[t-1]
        N, K = puzzle.pop()
        result = 0

        # 퍼즐의 가로에서 길이가 K인 문자가 들어갈 수 있는 개수를 구한다.
        for row in range(N):
            one = 0
            for col in range(N):
                if puzzle[row][col] == 1:
                    one += 1
                else:
                    if one == K:
                        result += 1
                    one = 0
            if one == K:
                result += 1
        
        # 퍼즐의 세로에서 길이가 K인 문자가 들어갈 수 있는 개수를 구한다.
        for col in range(N):
            one = 0
            for row in range(N):
                if puzzle[row][col] == 1:
                    one += 1
                else:
                    if one == K:
                        result += 1
                    one = 0
            if one == K:
                result += 1

        print(f'#{t} {result}')

solution()