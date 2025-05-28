'''예외처리'''

# 예외처리
try:
    print('[나누기 전용 계산기]')
    num1 = int(input('첫번째 숫자를 입력하세요: '))
    num2 = int(input('두번째 숫자를 입력하세요: '))
    print('{0}/{1}={2}' .format(num1, num2, int(num1/num2)))
except ValueError:
    print('에러! 잘못된 값을 입력하였습니다.')
except ZeroDivisionError as err:
    print(err)


# 에러
try:
    print('[한자리 숫자 나누기 계산기]')
    num3 = int(input('첫번째 숫자를 입력하세요: '))
    num4 = int(input('두번째 숫자를 입력하세요: '))
    if num3 >= 10 or num4 >= 10:
        raise ValueError # 새로 정의한 에러 강제 발생
    print('{0}/{1}={2}' .format(num3, num4, int(num3/num4)))
except ValueError:
    print('에러! 잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.')


# 에러처리 사용자화
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print('[한자리 숫자 나누기 계산기(사용자화)]')
    num5 = int(input('첫번째 숫자를 입력하세요: '))
    num6 = int(input('두번째 숫자를 입력하세요: '))
    if num5 >= 10 or num6 >= 10:
        raise BigNumberError('입력값: {0}, {1}' .format(num5, num6))
    print('{0}/{1}={2}' .format(num5, num6, int(num5/num6)))
except BigNumberError as err:
    print('에러(사용자화)! 잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.')
    print(err)
finally:
    print('[계산기 사용 종료]')


# QUIZ
chicken = 10
waiting = 1

class SoldoutError(Exception):
    pass

while(True):
    try:
        print('[남은 치킨: {0}]' .format(chicken))
        order = int(input('치킨을 몇마리 주문하시겠습니까? '))
        if order > chicken:
            print('! 재료가 부족합니다.')
        elif order <= 0:
            raise ValueError
        else:
            print('대기번호 {0}: {1}마리 주문이 완료되었습니다.' .format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0:
            raise SoldoutError
    except ValueError:
        print('! 잘못된 값을 입력했습니다.')
    except SoldoutError:
        print('! 재고가 소진되어 더 이상 주문을 받지 않습니다.')
        break

