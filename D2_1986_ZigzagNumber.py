"""
Problem : D2 1986 지그재그 숫자(Zigzag Number)
1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 누적된 값을 구해보자.
예제 : N이 5일 경우, 1 - 2 + 3 - 4 + 5 = 3

N은 1 이상 10 이하의 정수이다.

가장 첫 줄에서는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.

각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 누적된 값을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    # 테스트 케이스의 개수 T
    T = int(input())

    # 테스트 케이스 test_case
    test_case = []
    
    # T번 반복하며, 테스트 케이스를 입력받는다.
    for _ in range(T):
        test_case.append(int(input()))
    
    # T번 반복하며, 각 테스트 케이스의 결과를 출력한다.
    for t in range(1, T+1):
        N = test_case[t-1]
        # 누적된 결과 값 result
        result = 0
        for n in range(1, N+1):
            # n이 홀수라면 더한다.
            if n % 2 == 1:
                result += n
            # n이 짝수라면 뺀다.
            else:
                result -= n
        # 누적된 결과 값을 출력한다.
        print(f'#{t} {result}')

solution()