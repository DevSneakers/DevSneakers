# 실습예제 3
# lyric.txt는 애국가 가사. 파일의 가사 순서를 살펴보고, 1에서 4사이의 정수를 입력받아 정수에 해당하는 절의 가사를 후렴 포함 출력.
a = int(input("몇 절을 출력할지 입력하세요 : "))
input_list = ['무궁화 삼천리 화려강산\n', '대한사람 대한으로 길이 보전하세\n']
input_lyric =  [['동해물과 백두산이 마르고 닳도록\n', '하느님이 보우하사 우리나라 만세\n'],
                ['남산 위에 저 소나무 철갑을 두른 듯\n', '바람 서리 불변함은 우리 기상일세\n'],
                ['가을 하늘 공활한데 높고 구름 없이\n', '밝은 달은 우리 가슴 일편단심일세\n'],
                ['이 기상과 이 맘으로 충성을 다하여\n', '괴로우나 즐거우나 나라 사랑하세\n']]

f = open("lyric.txt",'w')

for idx in range(4):
    if a == idx:
        f.write(str(input_lyric[idx-1]))
        f.write(str(input_list))

f = open("lyric.txt", 'r')


f.close()

