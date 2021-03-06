"""
Problem : D1 2025 N줄 덧셈(N Line Addition)
1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.
단, 주어질 숫자는 10,000을 넘지 않는다.

주어진 숫자가 10 일 경우 출력해야 할 정답은,
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
"""

def solution():
    # 주어진 숫자 N
    N = int(input())
    # 등차수열의 합 사용, 등차수열의 합 : n/2(2a(1) + (n-1)d), a(1) : 초항, d : 등차
    # 초항이 1, 등차가 1인 등차수열의 합 : n/2(n+1)
    result = (N**2 + N) / 2
    print(int(result))

solution()