# 실습예제 2
# lines.txt는 영소문자, 숫자, 줄바꿈으로 이루어진 텍스트 파일. 마지막 줄부터 첫줄까지 역순으로 출력

f = open("lines.txt",'w')
input_list = ["app1es\n", "b1ack22\n", "can334dy\n", "dra2013ma\n", "e443gg55\n", "flyyy24\n"]
for i in input_list:
    f.write(i)

f = open("lines.txt",'r')

output_list= f.readlines()
output_list.reverse()

for j in output_list:
    print(j)

f.close()