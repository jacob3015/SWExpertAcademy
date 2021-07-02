"""
Problem : D2 1859 백만장자 프로젝트(Millionaire Project)

25년 간의 수행 끝에 원재는 미래를 보는 능력을 갖게 되었다. 이 능력으로 원재는 사재기를 하려고 한다.
다만 당국의 감시가 심해 한 번에 많은 양을 사재기 할 수 없다.
다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주자.
1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
3. 판매는 얼마든지 할 수 있다.
예를 들어 3일 동안의 매매가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.

첫번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스 별로 첫 줄에는 자연수 N(2 <= N <= 1,000,000)이 주어지고,
둘째 줄에는 각 날의 매매가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다.
각 날의 매매가는 10,000이하이다.

각 테스트 케이스마다 '#x'(x는 테스트 케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 최대 이익을 출력한다.
"""

def solution():
    # 테스트 케이스의 수 T
    T = int(input())
    # 결과를 저장할 result
    result = []
    # T번 반복하며, 테스트 케이스 결과를 result에 append 한다.
    for _ in range(T):
        # 예측 가능한 일 수 N
        N = int(input())
        # 예측 가능한 가격 price
        price = list(map(int, input().split()))
        # 수익 profit
        profit = 0
        # 현재 최고가 max_price
        max_price = 0
        # price를 뒤에서 부터 탐색하기 위해 reverse() method 사용
        price.reverse()
        """
        price를 앞에서 부터 완전 탐색 하는 경우의 시간복잡도 : O(N**2)
        price를 뒤에서 부터 완전 탐색 하는 경우의 시간복잡도 : O(N)

        앞에서 부터 완전 탐색을 수행하게 되면 매번 현재 가격과 미래의 가격 중 최고가를 구해 비교해야 한다.
        현재의 가격이 price[d]일 때, 현재 가격을 포함한 미래의 가격 중 최고가는 max(price[d:day]) 로 구할 수 있다.
        이 때, max() method는 주어진 iterable 자료형을 완전 탐색해 그중 가장 큰 수를 반환한다.
        따라서 max() method를 사용하게 되면 O(N**2)의 시간복잡도를 가진다.

        반면, price를 뒤에서부터 완전 탐색하는 경우 최고가를 update하는 방식을 사용하기 때문에 매번 최고가를 따로 구할 필요가 없다.
        따라서 뒤에서부터 완전 탐색하는 경우 O(N)의 시간 복잡도를 가진다.
        """
        # reverse() method로 반전된 price를 완전 탐색 한다.
        for p in price:
            # 현재 가격 p가 기존의 최고가 max_price보다 크거나 같다면, max_price를 update한다.
            if p >= max_price:
                max_price = p
            # 현재 가격 p가 기존의 최고가 max_price보다 작다면, 수익을 남긴다.
            else:
                profit += max_price - p
        result.append(profit)
    # 테스트 케이스 결과를 출력한다.
    for t in range(1, T+1):
        print(f'#{t} {result[t-1]}')

solution()