"""
Problem : 간단한 N 의 약수(Simple N Divisor)

입력으로 1개의 정수 N 이 주어진다.
정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

N은 1이상 1,000이하의 정수이다. (1 <= N <= 1,000)

입력으로 정수 N이 주어진다.

정수 N의 모든 약수를 오름차순으로 출력한다.
"""

def solution():
    # 정수 N
    N = int(input())
    # N의 모든 약수를 저장할 result
    result = []
    # N의 모든 약수를 구해 result 에 append 한다.
    for n in range(1, N+1):
        if N % n == 0:
            result.append(n)
    # 결과를 출력한다.
    for r in result:
        print(r, end=' ')

solution()