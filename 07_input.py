'''입출력'''

# 표준 입출력
print('python', 'java', 'javascript', sep=', ', end='? ')
# sep: seperate 출력 중간 제어
# end: 출력 끝부분 제어

import sys
print('a', 'b', file=sys.stdout) # 표준 출력
print('a', 'b', file=sys.stderr) # 표준 에러

scores = {'언어': 100, '수학': 0, '영어': 50}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(4), str(score).rjust(8), sep=":") # ljust: 왼쪽 정렬

for wait_num in range(1, 21):
    print('대기번호: ' + str(wait_num).zfill(3)) # zfill: n자리수로 0 채우기

# answer = input('입력하세요: ')
# print('입력하신 값은 ' + answer + '입니다.') # input 값은 항상 string 문자열로 받음


# 다양한 출력 포맷
print('{0: >10}' .format(500)) # space: 빈칸 / >: 오른쪽정렬 / 10: 10자리빈칸

print('{0: >+10}' .format(500)) # 양수일 때  + 표시
print('{0: >+10}' .format(-500)) # 음수일 때 - 표시

print('{0:_<10}' .format(500)) # _: 빈공간 / <: 왼쪽정렬 / 10: 10자리빈칸

print('{0:,}' .format(100000000)) # ,: 3자리마다 ,
print('{0:+,}' .format(100000000))
print('{0:^<+30,}' .format(100000000000000))

print('{0:f}' .format(5/3)) # f: 소수점
print('{0:.2f}' .format(5/3)) # .2: 소수점 2째자리에서 반올림


# 파일 입출력
score_file = open('input_test.txt', 'w', encoding='utf8') # txt 파일이 생성됨 (print 안 내용)
print('수학: 0', file=score_file)
print('영어: 50', file=score_file)
score_file.close()

score_file = open('input_test.txt', 'a', encoding='utf8')
score_file.write('과학: 80') # 줄바꿈X -> \n 필요
score_file.write('\n언어: 100')
score_file.close()

score_file = open('input_test.txt', 'r', encoding='utf8') # r: read
print(score_file.read())
score_file.close()

# score_file = open('input_test.txt', 'r', encoding='utf8')
# print(score_file.readline()) # 줄별로 읽기
# print(score_file.readline()) 
# score_file.close()

# score_file = open('input_test.txt', 'r', encoding='utf8')
# while True: # 반복문 통해 파일 내용 가져오기
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end=' ')
# score_file.close()

# score_file = open('input_test.txt', 'r', encoding='utf8')
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end=' ')
# score_file.close()


# pickle
import pickle
profile_file = open('pickle_test.pickle', 'wb') #wb: write binary
profile = {'name': 'Blue', 'age': '30', 'hobby': ['a', 'b', 'c']}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open('pickle_test.pickle', 'rb')
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()


# with : 파일 매번 닫을 필요X
import pickle
with open('pickle_test.pickle', 'rb') as profile_file: 
    # pickle_test.pickle 내용을 profile_file 변수로 저장
    print(pickle.load(profile_file))
    # profile_file 변수를 불러와서 pickle을 통해 출력

with open('test.txt', 'w', encoding='utf8') as study_file:
    study_file.write('testing')

with open('test.txt', 'r', encoding='utf8') as study_file:
    print(study_file.read())


# QUIZ
for i in range(1, 4):
    with open('test_' + str(i) + '주차.txt', 'w', encoding='utf8') as report_file:
        report_file.write('-- {0}주차 주간 보고 --' .format(i))
        report_file.write('\n부서: ')
        report_file.write('\n이름: ')
        report_file.write('\n업무요약: ')
