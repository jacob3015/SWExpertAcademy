"""
Problem : D2 1959 두 개의 숫자열(Two Numeric Array)

N 개의 숫자로 구성된 숫자열 A와 M개의 숫자로 구성된 B가 있다.
A나 B를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
단, 더 긴 쪽의 양 끝을 벗어나서는 안된다.
서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최대값을 구하라.
N과 M은 3 이상 20 이하이다.

가장 첫 줄에는 테스트 케이스 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N과 M이 주어지고, 두 번째 줄에는 A, 세 번째 줄에는 B가 주어진다.

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    """두 개의 정수 리스트의 마주보는 위치를 변경해 원소끼리 곱한 뒤 합한 결과 중 최댓값을 출력한다.
    Extra explanation:
        두 개의 정수 리스트 중 길이가 더 짧은 리스트에 맞춰 길이가 더 긴 리스트를 완전 탐색해 결과를 구한다.

    Variables:
        T : 테스트 케이스의 개수
        test_case : 테스트 케이스 리스트
        N : A 정수 리스트의 길이
        M : B 정수 리스트의 길이
        A : 첫 번째 정수 리스트
        B : 두 번째 정수 리스트
        result : 두 개의 정수 리스트의 원소 끼리 곱한 뒤 합한 결과 리스트
        mul : 두 개의 정수 리스트의 원소 끼리 곱한 결과 리스트

    Example:
        >>> 1           : input T
        >>> 3 5         : input N, M
        >>> 1 5 3       : input A
        >>> 3 6 -7 5 4  : input B
        >>> #1 30       : output
    """
    T = int(input())
    test_case = []

    for _ in range(T):
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        test_case.append((A, B))

    for t in range(1, T+1):
        result = []
        A, B = test_case[t-1][0], test_case[t-1][1]
        N, M = len(A), len(B)

        if N > M:
            for n in range(N-M+1):
                mul = []
                for m in range(M):
                    mul.append(A[n+m] * B[m])
                result.append(sum(mul))
        else:
            for m in range(M-N+1):
                mul = []
                for n in range(N):
                    mul.append(A[n] * B[m+n])
                result.append(sum(mul))

        print(f'#{t} {max(result)}')

solution()