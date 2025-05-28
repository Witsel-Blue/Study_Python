'''모듈과 패키지'''

# 모듈
import module_test
module_test.price(3)
module_test.price_morning(4)
module_test.price_soldier(2)

# import module_test as mt
# mt.price(3)
# mt.price_morning(4)
# mt.price_soldier(2)

# from module_test import *
# price(3)
# price_morning(4)
# price_soldier(2)

# from module_test import price, price_morning
# price(1)
# price_morning(1)

# from module_test import price_soldier as ps
# ps(1)


# 패키지: 여러 모듈 파일을 담고 있는 디렉토리
import package_test.package1
playing = package_test.package1.Package1()
playing.detail()

# from package_test.package2 import Package2
# playing = Package2()
# playing.detail()

from package_test import *
playing = package2.Package2() # __init__ 파일에서 __all__ 설정 필요
playing.detail()


# 위치찾기
import inspect
print(inspect.getfile(package2))


# pip: 이썬 외부 패키지를 공식 저장소(PyPI)에서 다운로드하여 설치하고 관리하는 데 사용되는 표준 도구
# pip list: 패키지 리스트 확인


# 내장함수 builtins
# input: 사용자 입력을 받는 함수
# dir: 객체를 넘겼을 때 그 객체의 변수와 함수 표시
# 등등


# 외장함수 modules
import glob # glob: 경로 내 폴더, 파일 목록 조회
print(glob.glob('*.py'))

import os # os: 운영체제에서 제공하는 기본 기능
# print(os.getcwd()) # 현재 디렉토리

import time # time: 시간
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime # datetime
print(datetime.date.today())

today = datetime.date.today()
td = datetime.timedelta(days=100) # timedelta: 두 날짜 사이의 간격
print('D+100', today + td)