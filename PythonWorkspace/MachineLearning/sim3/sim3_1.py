# 실습예제 1
# lab1.txt 라는 이름으로 파일을 생성하고 두 정수 A, B를 입력받아, A+B, A-B, A*B의 값을 파일에 쓰는 프로그램
A = input("정수 1 입력 : ")
B = input("정수 2 입력 : ")
a = int(A)
b = int(B)

array = [str(a+b)+"\n", str(a-b)+"\n", str(a*b)+"\n"]

f = open("lab1.txt", 'w')
for i in array:
    f.write(i)

f = open("lab1.txt",'r')
print(f.read())

f.close()