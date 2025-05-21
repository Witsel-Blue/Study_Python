'''문자열'''

# 문자열 string
sentence = 'test'
print(sentence)

sentence2 = '''test
test
test'''

print(sentence2)


# 슬라이싱
jumin = '921129-1234567'

print('성별: ' + jumin[7])
print('년도: ' + jumin[0:2])
print('월: ' + jumin[2:4])
print('일: ' + jumin[4:6])
print('생년월일: ' + jumin[:6])
print('뒷자리: ' + jumin[7:])
print('뒷자리(거꾸로): ' + jumin[-3:])


# 문자열 처리 함수
test = 'I am testing'
print(test.lower())
print(test.upper())
print(test[0].isupper()) # 0번째 문자열이 대문자인지 체크
print(len(test)) # 문자열 전체 길이
print(test.replace('I am', 'Cat is'))

index = test.index('t')
print(index)
index = test.index('t', index + 1)
print(index)

print(test.find('t'))
print(test.find('hello'))
# print(test.index('hello'))

print(test.count('t'))


# 문자열 포맷
print('a' + 'b')
print('a', 'b')

print('오늘은 %d일입니다.' % 20)
print('오늘의 날씨는 %s입니다.' % '맑음')
print('Apple은 %c로 시작합니다.' % 'A')
print('나는 %s색과 %s색을 좋아합니다.' % ('파란', '빨간'))

print('오늘은 {}입니다.' .format(20))
print('나는 {}색과 {}색을 좋아합니다.' .format('파란', '빨간'))
print('나는 {1}색과 {0}색을 좋아합니다.' .format('파란', '빨간'))

print('오늘은 {date}일입니다. 오늘의 날씨는 {weather}입니다.' .format(date = 20, weather = '맑음'))

date = 20
weather = '맑음'
print(f'오늘은 {date}일입니다. 오늘의 날씨는 {weather}입니다.')


# 탈출 문자
print('백문이 불여일견\n백견이 불여일타') # \n : 줄바꿈
print('test "test"')
print('test \'test\'') # \' : ''
print('folder\\folder') # \\ : \
print('Red Apple\rPine') # \r : 커서를 맨 앞으로 이동
print('Redd\bApple') # \b : backspace (한 글자 삭제)
print('Red\tApple') # \t : tab


# QUIZ
url = 'http://google.com'
pwd = url.replace('http://', '')
pwd = pwd[:pwd.index('.')]
pwd = pwd[:3] + str(len(pwd)) + str(pwd.count('e')) + '!'

print(url + ' 비밀번호: ' + pwd)