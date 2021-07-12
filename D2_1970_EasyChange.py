"""
Problem : D2 1970 쉬운 거스름돈(Easy Change)

우리나라 화폐 '원'은 금액이 높은 돈을 우선적으로 계산할 때 돈의 개수가 가장 최소가 된다.
S마켓에서 사용하는 돈의 종류는 다음과 같다.
50,000원, 10,000원, 5,000원, 1,000원, 500원, 100원, 50원, 10원
S마켓에서 손님에게 거슬러 주어야 할 금액 N이 입력되면 돈의 최소 개수로 거슬러 주기 위하여 각 종류의 돈이 몇 개씩 필요한지 출력하라.

N은 10 이상 1,000,000 이하의 정수이다.
N의 마지막 자릿수는 항상 0이다.

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.

각 줄은 '#t'로 시작하고, 다음줄에 각 돈의 종류마다 필요한 개수를 빈칸 사이에 두고 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    """거슬러 주어야 할 금액을 입력 받아 총 돈의 개수가 최소가 되게하는 각 돈의 종류 별 필요한 개수를 출력한다.

    Variables:
        T : 테스트 케이스의 개수
        test_case : 주어진 테스트 케이스 리스트
        changes_list : 돈의 종류 리스트
        N : 거슬러 주어야 하는 돈
        results_list : 돈의 종류별 필요한 개수 리스트

    Example:
        >>> 1               : input T
        >>> 32850           : input test case
        >>> #1              : output test case number
        >>> 0 3 0 2 1 3 1 0 : output test case result
    """
    T = int(input())
    test_case = [int(input()) for t in range(T)]
    changes_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for t in range(1, T+1):
        N = test_case[t-1]
        results_list = []

        for change in changes_list:
            results_list.append(N//change)
            N -= (N//change) * change

        print(f'#{t}')
        for result in results_list:
            print(result, end=' ')
        print('')

solution()