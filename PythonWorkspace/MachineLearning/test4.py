# 4. 거꾸로 문자열
# 사용자로부터 문자열 sports를 입력 받아 거꾸로 출력

String = input("문자열 입력 : ")    # 변수 String에 문자열을 입력받음
n = 1                   # 변수 n 선언 및 1로 초기화
for i in String:        # String에서 i로 값을 가져올 for문 선언
    print(String[-n])   # 문자열 인덱싱으로 한 글자씩 출력
    n = n + 1           # 변수 n을 1씩 올려주며 print문이 거꾸로 출력할 수 있게 함