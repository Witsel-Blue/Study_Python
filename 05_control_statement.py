'''제어문'''

# if
# weather = input('오늘 날씨는 어때요? ')
# if weather == '비' or weather == '눈':
#     print('우산을 챙기세요')
# elif weather == '미세먼지':
#     print('마스크를 챙기세요')
# else:
#     print('날씨가 맑습니다')

# temp = int(input('기온은 어때요? '))
# if 30 <= temp:
#     print('너무 덥습니다.')
# elif 10 <= temp and temp < 30:
#     print('날씨가 좋습니다.')
# elif 0 <= temp < 10:
#     print('외투를 챙기세요')
# else:
#     print('너무 춥습니다.')


# for: 리스트처럼 정해진 대상을 순서대로 반복
for num in [0, 1, 2, 3,4]:
    print('number: {0}' .format(num))

for num in range(5):
    print('number: {0}' .format(num))

for num in range(1,6):
    print('number: {0}' .format(num))

names = ['a', 'b', 'c']
for name in names:
    print('{0}, hello' .format(name))


# while: 특정 조건이 참인 동안 계속 반복할 때
# customer = 'Blue'
# person = 'unknown'
# while person != customer :
#     print('{0}, 커피가 준비 되었습니다. ' .format(customer))
#     person = input('이름이 어떻게 되세요? ')


# continue / break
absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue # 현재 진행 중인 반복을 중단하고, 해당 반복문의 다음 단계로 넘어가도록 지시
    elif student in no_book:
        print('{0} has no book.' .format(student))
        break # 반복문 바로 종료
    print('{0}, read.' .format(student))


# for
lists = [1,2,3,4,5]
lists = [i+100 for i in lists]
print(lists)

lists2 = ['a', 'test']
lists2 = [len(i) for i in lists2]
print(lists2)


# QUIZ
from random import *
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15: 
        print('[O] {0}번째 손님 (소요시간: {1}분)' .format(i, time))
        cnt += 1
    else: 
        print('[ ] {0}번째 손님 (소요시간: {1}분)' .format(i, time))
print('총 탑승 승객: {0}분' .format(cnt))