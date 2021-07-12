"""
Problem : D2 1966 숫자를 정렬하자(Sorting Numbers)

주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.
N은 5이상 50 이하이다.

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 이 주어지고, 다음 줄에 N 개의 숫자가 주어진다.

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    """숫자열을 입력 받아 오름차순 정렬해 출력한다.

    Variables:
        T : 테스트 케이스의 개수
        test_case : 주어진 테스트 케이스 리스트
        N : 숫자열의 길이

    Example:
        >>> 1               : input T
        >>> 5               : input N
        >>> 1 4 7 8 0       : input number list
        >>> #1 0 1 4 7 8    : output number list sorted in ascending order
    """
    T = int(input())
    test_case = []

    for _ in range(T):
        N = int(input())
        test_case.append(list(map(int, input().split())))

    for t in range(1, T+1):
        print(f'#{t}', end=' ')
        test_case[t-1].sort()
        for result in test_case[t-1]:
            print(result, end=' ')
        print('')

solution()