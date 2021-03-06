"""Problem : D2 1288 새로운 불면증 치료법(New Cure for Insomnia)

민식이는 불면증에 걸렸다. 그래서 잡이 안 올 때의 민간요법 중 하나인 양 세기를 하려고 한다.
민식이는 1번 양부터 순서대로 세는 것이 재미없을 것 같아서 N의 배수 번호인 양을 세기로 하였다.
즉, 첫 번째에는 N번 양을 세고, 두 번째에는 2N번 양, k번째에는 kN번 양을 센다.
이렇게 숫자를 세던 민석이에게 잠은 더 오지 않고 다음과 같은 궁금증이 생겼다.
이전에 셌던 번호들의 각 자리수에서 0 에서 9 까지의 모든 숫자를 보는 것은 최소 몇 번 양을 센 시점일까?
예를 들어 N = 1295 이라고 하자.
첫 번째로 N = 1295번 양을 센다. 현재 본 숫자는 1, 2, 5, 9 이다.
두 번째로 2N = 2590번 양을 센다. 현재 본 숫자는 0, 2, 5, 9 이다.
현재까지 본 숫자는 0, 1, 2, 5, 9 이다.
이런식으로 계속해서 양을 세다 0 부터 9 까지 모든 숫자를 한번 이상 보게 되는건 최소 몇 번 양을 센 시점인지 구해라.

첫 번째 줄에 테스트 케이스의 수 T 가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 N 이 주어진다.

각 테스트 케이스마다 '#t'를 출력하고, 한 칸 띄고 결과를 출력한다.
(t는 테스트 케이스 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    """주어진 N 을 기준으로 0 부터 9 까지의 수를 최소 한번 이상 보게 되려면 최소 몇 번 양을 센 시점인지 구해 출력한다.
    Extra explanation:
        0 부터 9 까지의 수가 등장하는 횟수를 count하는 방식으로 0 부터 9 까지 최소 한번 이상 등장하는 시점을 구한다.
        예를 들어, 1N = 1290 일 때 numbers = [1, 1, 1, 0, 0, 0, 0, 0, 0, 1] 이런식으로 수의 등장 횟수를 count하는 방법을 사용한다. 

    Variables:
        T : 테스트 케이스의 개수
        test_case : 주어진 테스트 케이스 리스트
        N : 양을 세는데 기준이 되는 정수
        numbers : 양을 셀 때 0 부터 9 까지의 등장 횟수를 저장하는 리스트
        count : 양을 센 횟수
    
    Example:
        >>> 1       : input T
        >>> 1295    : input N
        >>> #1 6475 : output (count*N)
    """
    T = int(input())
    test_case = [int(input()) for _ in range(T)]

    for t in range(1, T+1):
        N = test_case[t-1]
        numbers = [0 for _ in range(10)]
        count = 0
        
        while 0 in numbers:
            count += 1
            for n in str(N*count):
                numbers[int(n)] += 1

        print(f'#{t} {count*N}')

solution()