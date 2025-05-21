'''연산자'''

# 연산자

print(1+1)
print(3-2)
print(2*3)
print(6/2)

print(2**3) # 2^3
print(5%3) # 5 나누기 3 값의 나머지
print(10//3) # 10 나누기 3의 몫

print(10 > 3)
print(4 <= 4)

print(3 == 3)
print(1 == 2+3)

print(1 != 3)
print(not(1 != 3))

print((3 > 0 ) and (3 < 5)) # true and true -> true
print((3 > 0 ) & (3 < 5))

print((3 > 0 ) or (3 > 5)) # true or false -> true
print((3 > 0 ) | (3 > 5))

print(5 > 4 > 3) # true and true -> true
print(5 > 4 > 7) # true and false -> false


# 수식
number = 2 + 3 * 4
print(number)

number = number + 2
print(number)

number += 2
print(number)

number *= 2
print(number)

number /= 2
print(number)

number -= 2
print(number)

number %= 5 # 16을 5로 나눴을 때의 나머지값
print(number)


# 숫자처리 함수
print(abs(-5)) # absolute 절대값
print(pow(4, 2)) # 4^2
print(max(5, 12)) # 최대값
print(min(5, 12)) # 최소값
print(round(3.14)) # 반올림

from math import *
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근


# 랜덤 함수
from random import *
print(random()) # 0.0이상 1.0미만의 임의의 값 생성
print(random() * 10)
print(int(random() * 10))

print(int(random() * 45) + 1)
print(randrange(1, 46))
print(randint(1, 45))


# QUIZ
date = int(randint(4, 28))
print('오프라인 스터디 모임 날짜는 매월 ' + str(date) + '일로 선정되었습니다.')