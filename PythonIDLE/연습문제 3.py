# Q2
# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자
a = 1
sum = 0
while a <= 1000:
    if a % 3 == 0:
        sum = sum + a
    a = a + 1

print(sum)


# Q3
# while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해보자
a = 0

while a < 6:
    print("*" * a)
    a = a + 1

# Q4
# for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
a = 0

for a in range(1, 101):
    print(a)

# Q5
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수를 구해보자.
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
avg = 0
times = 0

for i in a:
    sum = sum + i
    print(i)
    times = times + 1
    
avg = sum / times

print(int(avg))


