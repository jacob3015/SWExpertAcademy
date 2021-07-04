"""
패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.

각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 길이가 30인 문자열이 주어진다.

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하여 1부터 시작한다.)
"""

def solution():
    # 테스트 케이스의 개수 T
    T = int(input())
    # 테스트 케이스를 저장할 test_case
    test_case = []
    # T번 반복하며, 테스트 케이스를 입력 받는다.
    for _ in range(T):
        test_case.append(input())
    # T번 반복하며, 문자열 slicing으로 주어진 문자열에서 반복되는 마디를 찾아 결과를 출력한다.
    for t in range(1, T+1):
        string = test_case[t-1]
        # 부분 문자열의 길이를 2부터 10까지 탐색해가며 마디를 찾아 마디의 길이를 출력한다.
        for s in range(1, 10):
            if string[:s] == string[s:s*2]:
                print(f'#{t} {len(string[:s])}')
                break

solution()