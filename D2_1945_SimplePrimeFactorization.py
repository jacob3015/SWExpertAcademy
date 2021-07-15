"""Problem : D2 1945 간단한 소인수분해(Simple Prime Factorization)
숫자 N은 아래와 같다.
N = 2^a * 3^b * 5^c * 7^d * 11^e
N이 주어질 때 a, b, c, d, e 를 출력하라.

N은 2 이상 10,000,000 이하이다.

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    """주어진 수 N(N = 2^a * 3^b * 5^c * 7^d * 11^e)을 소인수분해 구한 a, b, c, d, e를 출력한다.

    Variables:
        T : 테스트 케이스의 개수
        test_case : 주어진 테스트 케이스 리스트
        number : 주어진 N
        result : N을 소인수분해해 얻은 결과 리스트
    
    Example:
        >>> 1               : input T
        >>> 6791400         : input N
        >>> #1 3 2 2 3 1    : output result
    """
    T = int(input())
    test_case = [int(input()) for _ in range(T)]

    for t in range(1, T+1):
        number = test_case[t-1]
        result = [0 for _ in range(5)]

        while number > 1:
            if number % 11 == 0:
                result[4] += 1
                number //= 11
            if number % 7 == 0:
                result[3] += 1
                number //= 7
            if number % 5 == 0:
                result[2] += 1
                number //= 5
            if number % 3 == 0:
                result[1] += 1
                number //= 3
            if number % 2 == 0:
                result[0] += 1
                number //= 2

        print(f'#{t}', end=' ')
        for r in result:
            print(r, end=' ')
        print('')

solution()