"""
Problem : D1 2058 자릿수 더하기(Add Digits)

하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.

자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)

입력으로 자연수 N이 주어진다.

각 자릿수의 합을 출력한다.
"""

def solution():
    N = input()
    result = 0
    for n in N:
        result += int(n)
    print(result)

solution()