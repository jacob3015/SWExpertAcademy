"""
Problem : D1 2050 알파벳을 숫자로 변환(Convert Alphabet to Numeric)

알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.

문자열의 최대 길이는 200이다.

각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다.
"""

def solution():
    # 알파벳으로 이루어진 문자열 Alpha
    Alpha = input()
    # 알파벳을 정수로 변환한 결과 result
    result = []
    # ord() method로 알바벳을 정수로 변환한다. 이때, ord(A)=65, ord(Z)=90 이므로, 64를 빼준다.
    for a in Alpha:
        result.append(ord(a) - 64)
    # 변환 결과를 출력한다.
    for r in result:
        print(r, end=" ")

solution()