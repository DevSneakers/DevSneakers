# 1. 2 - 9 사이의 자연수(N)를 입력 받아서 구구단을 출력하는 프로그램을 구현하세요.
n = int(input("GuGu-Table : "))             # 정수형 변수 n선언 및 사용자에게 입력받음
result = 0                                  # 결과값 저장할 result 변수 선언

for i in range(9):                          # 구구단 반복출력을 위한 for문 선언
    i = i + 1                               # range 함수는 0부터 시작하기 때문에 i에 1을 더함
    result = n * i                          # 연산 결과 result 에 저장
    print("%d X %d = %d" % (n, i, result))  # 결과값 출력