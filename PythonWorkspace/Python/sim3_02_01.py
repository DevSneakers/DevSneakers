# 실습예제 2
grade = []
a = ['학번을', '이름을', '국어점수를', '영어점수를', '수학점수를']

for i in range(len(a)):
    if a[i] == '이름을':
        grade.append(input(a[i] + " 입력하세요 : "))
    else:
        grade.append(int(input(a[i] + " 입력하세요 : ")))

print(grade)