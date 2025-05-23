'''함수'''

# 함수 : 반복되거나 특정 기능을 수행하는 코드들을 하나의 블록으로 묶어 이름을 붙인 것
def open_account():
    print('새로운 계좌가 생성되었습니다.')

open_account()

# 전달값 / 반환값
def deposit(balance, money):
    print('입금이 완료되었습니다. 잔액은 {0}원입니다.' .format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print('출금이 완료되었습니다. 잔액은 {0}원입니다.' .format(balance - money))
        return balance - money
    else:
        print('출금이 완료되지 않았습니다. 잔액은 {0}원입니다.' .format(balance))
        return balance
    
def widthdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
print(balance)

balance = withdraw(balance, 2000)
print(balance)

balance = withdraw(balance, 500)
print(balance)

commission, balance = widthdraw_night(balance, 200)
print('수수료 {0}원이며 잔액은 {1}원입니다.' .format(commission, balance))


# 기본값
# def profile(name, age, main_lang):
#     print('이름: {0}\t나이: {1}\t주 사용 언어: {2}' \
#           .format(name, age, main_lang))

# profile('A', 20, 'python')
# profile('B', 25, 'java')

def profile(name, age=17, main_lang='python'):
    print('이름: {0}\t나이: {1}\t주 사용 언어: {2}' \
          .format(name, age, main_lang))

profile('A')
profile('B')


# 키워드값
def profile2(name, age, main_lang):
    print(name, age, main_lang)

profile2(main_lang='python', name='C', age='20') # 키워드 존재 시 순서 바껴도 호출 정렬 가능


# 가변인자
# def profile3(name, age, lang1, lang2, lang3, lang4, lang5):
#     print('name: {0}\t age: {1}\t' .format(name, age), end=' ') # end=' ': 줄바꿈 X
#     print(lang1, lang2, lang3, lang4, lang5)

def profile3(name, age, *language):
    print('name: {0}\t age: {1}\t' .format(name, age), end=' ') # end=' ': 줄바꿈 X
    for lang in language:
        print(lang, end=' ')
    print()

profile3('A', 20, 'python', 'java', 'javascript', 'c', 'c++', 'c#')
profile3('B', 25, 'Kotlin', 'Swift')


# 지역변수 / 전역변수
gun = 10

def checkpoint(soldiers):
    global gun # 전역공간에 있는 전역변수 사용
    gun = gun - soldiers
    print('[함수 내] 남은 총: {0}' .format(gun))

print('전체 총: {0}' .format(gun))
checkpoint(2)
print('남은 총: {0}' .format(gun))


gun2 = 20
def checkpoint_ret(gun2, soldiers):
    gun2 = gun2 - soldiers
    print('[함수 내] 남은 총: {0}' .format(gun2))

print('전체 총: {0}' .format(gun2))
gun2 = checkpoint_ret(gun2, 2)
print('남은 총: {0}' .format(gun2))


# QUIZ
def std_weight(height, gender):
    if gender == 'male':
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = 'male'
weight = round(std_weight(height / 100, gender), 2)

print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다.' \
      .format(height, gender, weight))