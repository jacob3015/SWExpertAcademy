"""Problem : D2 1928 Base64 Decoder

Encoding은 다음과 같이 한다.
1. 우선 24비트 버퍼에 위쪽부터 한 byte씩 3 byte의 문자를 집어넣는다.
2. 버퍼의 위쪽부터 6비트씩 잘라 그 값을 읽고, 각각의 값을 아래의 문자로 Encoding 한다.

문자 : 값
A : 0 ~ Z : 25, a : 26 ~ z : 51, 0 : 52 ~ 9 : 61, + : 62, / : 63

입력으로 Base64 Encoding 된 string 이 주어졌을 때, 해당 String 을 Decoding 하여, 원문을 출력하는 프로그램을 작성하시오.

문자열의 길이는 항상 4의 배수로 주어진다.
그리고 문자열의 길이는 100,000 을 넘지 않는다.

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스는 Encoding 된 상태로 주어지는 문자열이다.

테스트 케이스 t에 대한 결과는 '#t'을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

def solution():
    """Base64로 encoding 되어 주어진 문자열을 decoding 하여 원문을 출력한다.
    Extra explanation:
        Base64 Encoding 된 문자열을 ord() method를 이용해 ascii code로 변환한 값을 Base64 Encoding 된 값으로 사용하기 위해 변환 작업을 거친다.
        ord('A') = 65, ord('Z') = 90, ord('a') = 97, ord('z') = 122, ord('0') = 48, ord('9') = 57, ord('+') = 43, ord('/') = 47
        ord() method로 변환한 값의 Base64 맞춤 작업 후 6자리 2진수로 변환한다.
        6자리 2진수로 변환한 값을 8자리 2진수로 잘라 읽어 문자열의 원문을 복원한다.
    
    Variables:
        T : 테스트 케이스의 개수
        test_case : 주어진 테스트 케이스 리스트
        encoded_string : 주어진 Base64 encoded string
        decoded_binary : Base64 encoded string을 6자리 2진수로 변환한 string
        string_to_ascii : Base64 encoded string을 변환한 ascii code
        ascii_to_binary : Base64 맞춤 작업 후 변환한 2진수
        zero : ascii_to_binary를 6자리 2진수로 만들기 위해 필요한 0의 개수
        decoded_string : 복원된 원문 string
        binary : decoded_binary를 8자리 2진수로 slicing 한 string
        decimal : binary를 변환한 10진수

    Example:
        >>> 1                                       : input T
        >>> TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u    : input test case
        >>> #1 Life itself is a quotation.          : output
    """
    T = int(input())
    test_case = [input() for _ in range(T)]

    for t in range(1, T+1):
        encoded_string = test_case[t-1]

        decoded_binary = ''
        for ens in encoded_string:
            string_to_ascii = ord(ens)
            if 65 <= string_to_ascii <= 90:
                string_to_ascii -= 65
            elif 97 <= string_to_ascii <= 122:
                string_to_ascii -= 71
            elif 48 <= string_to_ascii <= 57:
                string_to_ascii += 4
            elif string_to_ascii == 43:
                string_to_ascii += 19
            else:
                string_to_ascii += 16

            ascii_to_binary = format(string_to_ascii, 'b')
            zero = 6 - (len(str(ascii_to_binary)) % 6)
            if zero < 6:
                ascii_to_binary = ('0' * zero) + str(ascii_to_binary)
            decoded_binary += str(ascii_to_binary)

        decoded_string = ''
        for de_bin in range(0, len(decoded_binary), 8):
            binary = decoded_binary[de_bin:de_bin+8]
            decimal = 0
            for bin in range(len(binary)):
                if int(binary[bin]) > 0:
                    decimal += (int(binary[bin]) * 2)**(7-bin)
            decoded_string += chr(decimal)
        
        print(f'#{t} {decoded_string}')

solution()