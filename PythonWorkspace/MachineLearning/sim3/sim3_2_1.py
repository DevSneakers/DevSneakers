# 실습예제 2
# lines.txt는 영소문자, 숫자, 줄바꿈으로 이루어진 텍스트 파일. 마지막 줄부터 첫줄까지 역순으로 출력
input_list = ["app1es\n", "b1ack22\n", "can334dy\n", "dra2013ma\n", "e443gg55\n", "flyyy24\n"]
f = open("lines.txt",'w')

for i in input_list:
    f.write(i)

f = open("lines.txt",'r')

output_list = f.read().split('\n')

del output_list[-1]
output_list.reverse()

for j in output_list:
    print(j)

f.close()