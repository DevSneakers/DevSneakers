# 실습예제 2 : 리스트 입출력
# 성적표를 만드려고 합니다. 사용자에게서 학번, 이름, 국어, 영어, 수학 점수를 입력받아 5가지 정보를 성적표 리스트로 작성하세요.
# 이때, 이름을 제외한 정보는 모두 숫자 데이터여야 합니다.
a = []
b = ['학번을', '이름을', '국어점수를', '영어점수를', '수학점수를']
num = 0

'''while num < len(b):
    if b[num] == '이름을':
        a.append(input(b[num]+ " 입력하세요 : "))
        num += 1
    a.append(int(input(b[num]+ " 입력하세요 : ")))
    num += 1
print(a)'''

for i in b:
    if i == '이름을':
        a.append(input(i + " 입력하세요 : "))
    else:
        a.append(int(input(i + " 입력하세요 : ")))
print(a)