"""
Problem : D2 2005 파스칼의 삼각형(Pascal's Triangle)

크기가 N인 파스칼의 삼각형을 만들어야 한다.
파스칼의 삼각형이란 아래와 같은 규칙을 따른다.
1. 첫 번째 줄은 항상 숫자 1이다.
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.

파스칼의 삼각형의 크기 N은 1이상 10 이하의 정수이다.

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.

각 줄은 #t로 시작하고, 다음 줄부터 파스칼의 삼각형을 출력한다.
삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    # 테스트 케이스의 개수
    T = int(input())
    # 테스트 케이스 test_case
    test_case = []
    # T번 반복하며, 테스트 케이스를 입력 받는다.
    for _ in range(T):
        test_case.append(int(input()))
    # T번 반복하며, 주어진 테스트 케이스에 대한 파스칼의 삼각형을 출력한다.
    for t in range(1, T+1):
        # 삼각형의 크기 N
        N = test_case[t-1]
        # 삼각형 triangle
        triangle = [([0]*N) for i in range(N)]
        # 파스칼의 삼각형을 구한다.
        for row in range(N):
            for col in range(N):
                if row == col:
                    triangle[row][col] = 1
                    break
                if col == 0:
                    triangle[row][col] = 1
                    continue
                triangle[row][col] = triangle[row-1][col-1] + triangle[row-1][col]
        # 주어진 테스트 케이스에 대한 파스칼 삼각형을 출력한다.
        print(f'#{t}')
        for row in range(N):
            for col in range(N):
                if row >= col:
                    print(triangle[row][col], end=' ')
            print('')

solution()