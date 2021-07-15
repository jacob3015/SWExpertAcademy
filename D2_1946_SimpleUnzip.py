"""Problem : D2 1946 간단한 압축 풀기(Simple Unzip)
원본 문서는 너비가 10인 여러 줄의 문자열로 이루어져 있다.
문자열은 마지막 줄을 제외하고 빈 공간 없이 알파벳으로 채워져 있고 마지막 줄은 왼쪽부터 채워져 있다.
이 문서를 압축한 문서는 알파벳과 그 알파벳의 연속된 개수로 이루어진 쌍들이 나열되어 있다.
압축된 문서를 입력 받아 원본 문서를 만드는 프로그램을 작성하시오.

압축된 문서의 내용
A 10
B 7
C 5

압축을 풀었을 때 원본 문서의 내용
AAAAAAAAAA
BBBBBBBCCC
CC

압축된 문서의 알파벳과 숫자 쌍의 개수 N은 1 이상 10 이하의 정수이다.
주어지는 알파벳은 A~Z의 대문자이다.
알파벳의 연속된 개수로 주어지는 수는 1 이상 20 이하의 정수이다.
원본 문서의 너비는 10으로 고정이다.

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어지고 다음 줄부터 N+1 줄까지 알파벳과 알파벳의 연속된 개수가 사이에 빈칸을 두고 주어진다.

각 줄은 '#t'로 시작하고, 다음 줄부터 원본 문서를 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    """주어진 압축된 문서를 입력 받아 원본 문서로 복원해 출력한다.

    Variables:
        T : 테스트 케이스의 개수
        test_case : 주어진 테스트 케이스 리스트
        N : 압축된 문서의 알파벳과 숫자 쌍의 개수
        documnet : 압축된 문서의 줄넘김 없는 원본 내용
        alpha : 압축된 문서의 알파벳
        alpha_num : 압축된 문서 각 알파벳의 개수
        count : 한줄에 나열된 문자의 개수

    Example:
        >>> 1           : input T
        >>> 3           : input N
        >>> A 10        : input compressed documnet
        >>> B 7
        >>> C 5
        >>> AAAAAAAAAA  : output uncompressed document
        >>> BBBBBBBCCC
        >>> CC
    """
    T = int(input())
    test_case = []

    for _ in range(T):
        N = int(input())
        document = ''
        for _ in range(N):
            alpha, alpha_num = map(str, input().split())
            document += (alpha * int(alpha_num))
        test_case.append(document)

    for t in range(1, T+1):
        document = test_case[t-1]
        count = 0
        print(f'#{t}')
        for alpha in document:
            count +=1
            print(alpha, end='')
            if count == 10:
                print('')
                count = 0
        print('')

solution()