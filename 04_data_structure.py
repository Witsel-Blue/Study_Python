'''자료구조'''

# 리스트 list : 순서O, 중복O
list0 = [10, 20, 30]
print(list0)

str_list = ['a', 'b', 'c'] 
print(str_list.index('b')) # 리스트 순서

str_list.append('d') # 리스트 마지막 추가
print(str_list)

str_list.insert(1, 'test') # 리스트 중간 삽입
print(str_list)

str_list.pop() # 리스트 마지막 제거
print(str_list)

str_list.append('a')
print(str_list.count('a')) # 리스트 같은 개수 찾기

num_list = [5,2,4,3,1]
num_list.sort() # 숫자 리스트 정렬
print(num_list)

num_list.reverse() # 숫자 리스트 역순 정렬
print(num_list)

num_list.clear() # 리스트 전부 삭제
print(num_list)

mix_list = ['a', 20, True] # 다양한 자료형 함께 사용 가능
print(mix_list)

list1 = [1,2,3]
list2 = ['a', 'b']
list1.extend(list2) # 리스트 두개 합치기
print(list1)


# 사전 dictionary
cabinet = {3:'three', 100:'hundred'} # key가 num일 때
print(cabinet[3])
print(cabinet.get(100))

# print(cabinet[4]) # key가 없을 때 오류, 그 이후 코드는 실행 X
print(cabinet.get(4)) # key가 없을 때 오류, none 출력
print(cabinet.get(4, '사용가능'))

print(3 in cabinet)
print(4 in cabinet)

cabinet2 = {'A-1': 'test1', 'A-2': 'test2'} # key가 str일 때
print(cabinet2['A-1'])

cabinet2['A-1'] = 'new1' # 교체
cabinet2['B-1'] = 'test3' # 추가
del cabinet2['A-2'] # 제거
print(cabinet2)

print(cabinet2.keys())
print(cabinet2.values())
print(cabinet2.items())

cabinet2.clear() # 전체 삭제
print(cabinet2)


# 튜플 tuple: 수정X
menu = ('pizza', 'pasta')
print(menu[0])

# menu.add('lasagna') # 추가는 불가능

(name, age, hobby) = ('cat', 4, 'sleep')
print(name, age, hobby)


# 집합 set : 순서X, 중복X
set0 = {1,2,3,3,3}
print(set0)

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd'}
print(set1 & set2) # 교집합
print(set1.intersection(set2)) # 교집합
print(set1 | set2) # 합집합
print(set1.union(set2)) # 합집합
print(set1 - set2) # 차집합
print(set1.difference(set2)) # 차집합

set1.add('e') # 추가
print(set1)

set1.remove('c') # 제거
print(set1)


# 자료 구조의 변경
bev = {'coffee', 'milk', 'juice'}
print(bev, type(bev))

bev = list(bev) # list []
print(bev, type(bev))

bev = tuple(bev) # tuple ()
print(bev, type(bev))

bev = set(bev) # set {}
print(bev, type(bev))


# QUIZ
from random import *
users = range(1, 21)
users = list(users)
shuffle(users)
print(users)

winners = sample(users, 4)

print('-- 당첨자 발표 --')
print('치킨 당첨자: {0}' .format(winners[0]))
print('커피 당첨자: {0}' .format(winners[1:]))