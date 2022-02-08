#문자열 안에 ",' 집어넣기
food = "\"Python is very ez.\" he says."

print(str(food))

#줄바꿈 문자열 한번에 초기화하기
multiline = '''
Life is too short
You need Python
'''

print(multiline)

#문자열 더하기
head = "Python"
tail = " likes shit"
sentence = head + tail

print(sentence)

#제목 설정 팁
print("="*50)
print("MY PROGRAM")
print("="*50)

#문자열 길이 구하기
a = "Life is too short"
print(len(a))

#문자열 인덱싱
a = "Life is too short, You need Python"
print(a[3])

#문자열 슬라이싱
print(a[0:4])

#슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]

print(date, weather)

#문자열 바꾸기
a = "Pithon"
print(a[:1] + 'y' + a[2:])
a = a[:1] + 'y' + a[2:]
print(a)

#문자열 포매팅
ex = "I ate %d apples." %3
print(ex)

ex = "I ate %s apples." %"five"
print(ex)

number = 10
day = "three"
ex = "I ate %d apples. so I was sick for %s days." %(number, day)

print(ex)

#문자열 포맷 코드
ex = "Error is %d%%." % 98
print(ex)

#포맷 코드와 숫자 함께 사용
#1. 정렬과 공백
ex = "%10s" %"hi"
print(ex)

ex = "%-10s" %"hi"
print(ex)

#2. 소수점 표현
ex = "%0.4f" %3.42134234
print(ex)

ex = "%10.4f" %3.42134234
print(ex)

#format 함수를 사용한 포매팅
#숫자 바로 대입
ex = "I eat {0} apples.".format(3)
print(ex)

#문자열 바로 대입
ex = "I eat {0} apples.".format("five")
print(ex)

#숫자 값을 가진 변수로 대입하기
number = 3
ex = "I eat {0} apples.".format(number)
print(ex)

#두 개 이상의 값 넣기
number = 10
day = "three"

ex = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(ex)

#이름으로 넣기
ex .format(3,"five")
print(ex)

ex1 = "%d, %s" %(number, day)
print(ex1)

ex = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(ex)

number = 3
day = "two"

ex = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(ex)

#인덱스 이름 혼용
ex = "I ate {0} apples. so I was sick for {day} days.".format(10, day = 3)
print(ex)

#왼쪽 정렬
ex = "{0:<10}".format("hi")
print(ex)

#오른쪽 정렬
ex = "{0:>10}".format("hi")
print(ex)

#가운데 정렬
ex = "{0:^10}".format("hi")
print(ex)

#공백 채우기
ex = "{0:=^10}".format("hi")
print(ex)

ex = "{0:!<10}".format("hi")
print(ex)

#소수점 표현하기
y = 3.42134234
ex = "{0:0.4f}".format(y)
print(ex)

ex = "{0:10.4f}".format(y)
print(ex)

#{ 또는 } 문자 표현하기

ex = "{{ and }}".format()
print(ex)

#f문자열 포매팅
name = '홍길동'
age = 30

ex = f'나의 이름은 {name} 입니다. 나이는 {age} 입니다.'
print(ex)

ex2 ='나의 이름은 {name} 입니다. 나이는 {age} 입니다.'
print(ex2)

ex = f"나는 내년이면 {age+1} 살이 된다."
print(ex)

d = {'name':'임꺽정','age':30}
ex = f'나의 이름은 {d["name"]} 입니다. 나이는 {d["age"]} 입니다.'
print(ex)

ex = f'{"hi":<10}'
print(ex)

ex = f'{"hi":>10}'
print(ex)

ex = f'{"hi":^10}'
print(ex)

ex = f'{"hi":=<10}'
print(ex)

ex = f'{"hi":=>10}'
print(ex)

ex = f'{"hi":=^10}'
print(ex)

y = 3.42134234
ex = f'{y:0.4f}'
print(ex)

ex = f'{y:10.4f}'
print(ex)

#문자열 관련 함수들
#count
a = "hobby"
b = a.count('b')
print(b)

#find
a = "Python is the best choice"
b = a.find('b')
print(b)

c = a.find('k')
print(c)

#index
a = "Life is too short"
b = a.index('t')
print(b)

c = a.index('o')
print(c)

#find와 index차이는 존재하지 않는 문자를 찾으면 find는 -1, index는 오류 리턴

#join
print(','.join('abcd'))

a = ",".join(['a','b','c','d'])
print(a)

#upper
a = "hi"
b = a.upper()
print(b)

#lower
c = b.lower()
print(c)

#lstrip(왼쪽 공백 지우기)
a = " hi "
print(a.lstrip())

#rstrip(오른쪽 공백 지우기)
print(a.rstrip())

#strip(양쪽 공백 지우기)
print(a.strip())

#replace
a = "Life is too short"
print(a.replace("Life", "Your legs"))

#split
a = "Life is too short"
b = a.split()
print(b)

c = "a:b:c:d"
d = c.split(':')
print(d)

#리스트 자료형

#리스트의 인덱싱
a = [1, 2, 3]
print(a)

print(a[0])

print(a[0]+a[2])

print(a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]

print(a[0])

print(a[-1])

print(a[3])

print(a[-1][0])

print(a[-1][1])

print(a[-1][2])

a = [1, 2, ['a', 'b', ['Life', 'is']]]

print(a[2][2][0])

#리스트 슬라이싱

a = [1, 2, 3, 4, 5]
print(a[0:2])

b = "12345"
print(a[0:2])

b = a[:2]
c = a[2:]

print(b)
print(c)

#중첩된 리스트에서 슬라이싱
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])

print(a[3][:2])

#리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

#리스트 반복
print(a*3)

#리스트 길이
print(len(a))

#리스트 연산 오류 예시
#a[2] + "hi" -> 3hi
print(str(a[2]) + "hi")

#리스트 값 수정
a[2] = 4
print(a)

#del 함수로 리스트 값 삭제
a = [1, 2, 3]
del a[1]

print(a)

a = [1, 2, 3, 4, 5]
del a[2:]

print(a)

#리스트 관련 함수
#리스트에 요소 추가(append)
a = [1, 2, 3]
a.append(4)

print(a)

a.append([5, 6])

print(a)

#리스트 정렬(sort)
a = [1, 4, 3, 2]
a.sort()

print(a)

a = ['a', 'c', 'b']
a.sort()

print(a)

#리스트 뒤집기(reverse)
a = ['a', 'c', 'b']
a.reverse()

print(a)

#위치 반환(index)
a = [1, 2, 3]

print(a.index(3))
print(a.index(1))

#요소 삽입(insert)
a = [1, 2, 3]
a.insert(0, 4)
print(a)

a.insert(3, 5)
print(a)

#리스트 요소 제거(remove)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

a.remove(3)
print(a)

#리스트 요소 끄집어내기(pop)
a = [1, 2, 3]
print(a.pop())
print(a)

a = [1, 2, 3]
print(a.pop(1))
print(a)

#리스트에 포함된 요소의 개수 세기(count)
a = [1, 2, 3, 1]
print(a.count(1))

#리스트 확장(extend)
a = [1, 2, 3]
a.extend([4, 5])
print(a)

b = [6, 7]
a.extend(b)
print(a)

#튜플
t1 = ()
t2 = (1, )  #1개의 요소만을 가질 때 ,를 반드시 붙인다.
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

#튜플 요솟값 삭제
t1 = (1, 2, 'a', 'b')


#튜플 요솟값 변경


#튜플 인덱싱
print(t1[0])

print(t1[3])

#튜플 슬라이싱
t1 = (1, 2, 'a', 'b')
print(t1[1:])

#튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
print(t1 + t2)

#튜플 곱하기
print(t2*3)

#튜플 길이 구하기
print(len(t1))


#딕셔너리 자료형

#기본 딕셔너리
#{Key1:Value1, Key2:Value2}

dic = {'name':'pey', 'phone': '0119993323', 'birth':'1118'}
a = {1:'hi'}
b = {'a':[1, 2, 3]}

#딕셔너리 쌍 추가, 삭제
#딕셔너리 쌍 추가
a = {1:'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3]
print(a)

#딕셔너리 요소 삭제
del a[1]
print(a)

#딕셔너리 사용법
#딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey':10, 'julliet':99}
print(grade['pey'])
print(grade['julliet'])

a = {1:'a', 2:'b'}
print(a[1])
print(a[2])

a = {'a':1, 'b':2}
print(a['a'])
print(a['b'])

print(dic['name'])
print(dic['phone'])
print(dic['birth'])

#딕셔너리 만들 때 주의사항
a = {1:'a', 1:'b'}
print(a)

#Key에 리스트는 쓸 수 없지만 튜플은 쓸 수 있다

#딕셔너리 관련 함수
#Key 리스트 만들기(keys)
print(list(dic.keys()))

for k in dic.keys():
    print(k)

#Value 리스트 만들기(values)
print(list(dic.values()))

#Key, Value 쌍 얻기(items)
print(list(dic.items()))

#Key:Value 쌍 지우기(clear)
dic.clear()

#Key로 Value 얻기(get)
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(a.get('name'))
print(a.get('phone'))

a = int(input("변수를 입력하세요 : "))
print(a + 1)