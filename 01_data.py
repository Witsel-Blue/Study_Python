'''자료형'''

# 숫자형 number
print(5)
print(-10)
print(3.14)
print(5+3)
print(3*(3+1))

# 문자형 string
print('test')
print("test2")
print('ㅋ'*9)

# 참/거짓 boolean
print(5>10)
print(5<10)
print(True)
print(not True)
print(not (5>10))

# 변수
animal = '고양이'
name = '진피즈'
age = 4
hobby = '낮잠'
is_adult = age >= 3

print('우리집 ' + animal + '의 이름은 ' + name + '이다.')
print(name + '는 ' + str(age) + '살이며, ' + hobby + '을 좋아한다.')
print(name, '는 ', age,'살이며, ', hobby, '을 좋아한다.')
print(name + '는 어른인가? ' + str(is_adult))