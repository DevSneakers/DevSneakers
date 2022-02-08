def add(a, b):
    return a + b

a = 3
b = 4
c = add(a, b)

print(c)

#매개변수와 인수

def add(a, b):      # a, b는 매개변수
    return a + b

print(add(3, 4))    # 3, 4는 인수

# 입력값과 결괏값에 따른 함수의 형태

# 일반적인 함수

def add(a, b):
    result = a + b
    return result

a = add(3, 4)
print(a)

# 입력값이 없는 함수

def say():
    return 'Hi'

a = say()
print(a)

