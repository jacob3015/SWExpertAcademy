"""
Problem : D2 1989 초심자의 회문 검사(Examine Palindrom)

"level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문이라 한다.
단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.

각 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 하나의 단어가 주어진다.

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    # 테스트 케이스의 개수 T
    T = int(input())

    # 테스트 케이스의 test_case
    test_case = []

    # T번 반복하며, 테스트 케이스를 입력 받는다.
    for _ in range(T):
        test_case.append(input())

    # T번 반복하며, 결과를 출력한다.    
    for t in range(1, T+1):
        # 주어진 테스트 케이스와 Extended slices를 이용해 반전된 테스트 케이스를 비교한다.
        if test_case[t-1] == test_case[t-1][::-1]:
            print(f'#{t} 1')
        else:
            print(f'#{t} 0')

solution()