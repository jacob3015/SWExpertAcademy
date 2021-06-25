"""
Problem : D1 2058 자릿수 더하기(Add Digits)

하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.

자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)

입력으로 자연수 N이 주어진다.

각 자릿수의 합을 출력한다.
"""

def solution():
    # 자연수 N을 string으로 입력 받는다.
    N = input()
    # 자릿수 합 result
    result = 0
    # 자연수 N의 자릿수를 하나씩 더한다.
    for n in N:
        result += int(n)
    # 자릿수의 합을 출력한다.
    print(result)

solution()