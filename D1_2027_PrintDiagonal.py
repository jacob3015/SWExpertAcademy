"""
Problem : D1 2027 대각선 출력하기(Print Diagonal)
주어진 텍스트를 그대로 출력하세요.

#++++
+#+++
++#++
+++#+
++++#
"""

def solution():
    for row in range(5):
        for col in range(5):
            if row == col : print('#', end='')
            else : print('+', end='')
        print('')

solution()