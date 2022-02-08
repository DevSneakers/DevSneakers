# 3. 양수만 출력
# numbers 라는 리스트가 주어졌을 때, 양수만 출력하는 프로그램을 작성하세요.
numbers = [1, -2, 3, -7, 8, -6, 11, 0]  # number 리스트 선언

for n in numbers:       # 리스트 number의 내용을 하나씩 비교하기 위한 for문 선언
    if n > 0:           # if문으로 n이 양수인지 검사
        print(n)        # n이 양수일 때 출력