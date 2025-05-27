'''클래스'''

# 클래스
# name = '마린'
# hp = 40
# damage = 5

# print('{} 유닛이 생성되었습니다.' .format(name))
# print('체력 {0}, 공격력 {1}\n' .format(hp, damage))

# tank_name = '탱크'
# tank_hp = 150
# tank_damage = 35

# print('{} 유닛이 생성되었습니다.' .format(tank_name))
# print('체력 {0}, 공격력 {1}\n' .format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]' .format(name, location, damage))

# attack(name, '1시', damage)
# attack(tank_name, '1시', tank_damage)

# class Unit:
#     def __init__(self, name, hp, damage): # __init__: 객체가 만들어질 때 필요한 초기 상태를 설정하는 역할
#         self.name = name # self: 현재 작업 중인 객체 인스턴스
#         self.hp = hp
#         self.damage = damage
#         print('{0} 유닛이 생성되었습니다.' .format(self.name))
#         print('체력 {0}, 공격력 {1}\n' .format(self.hp, self.damage))

# marine1 = Unit('마린', 40, 5)
# marine2 = Unit('마린', 40, 5)
# tank = Unit('탱크', 150, 35)
# self 제외 변수 모두 넣어줘야함


# 멤버변수
# wraith1 = Unit('레이스', 80, 5)
# print('유닛이름: {0}, 공격력: {1}' .format(wraith1.name, wraith1.damage))

# wraith2 = Unit('빼앗은 레이스', 80, 5)
# wraith2.clocking = True # 클래스 외부 변수 추가확장 가능

# if wraith2.clocking == True:
#     print('{0}는 현재 클로킹 상태입니다.' .format(wraith2.name))


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print('{0} 유닛이 생성되었습니다.' .format(name))

    def move(self, location): # 메소드: 클래스 안에 정의되어 객체의 기능이나 행동을 나타내는 함수
        print('{0}: {1}방향으로 이동합니다. [속도 {2}]'\
            .format(self.name, location, self.speed))
        
    def damaged(self, damage):
        print('{0}: {1} 데미지를 입었습니다.'\
            .format(self.name, self.hp))
        self.hp -= damage
        print('{0}: 현재 체력은 {1}입니다.'\
            .format(self.name, self.hp))
        if self.hp <= 0:
            print('{0}: 파괴되었습니다.' .format(self.name))

class AttackUnit(Unit): # 상속
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location): # 메소드
        print('{0}: {1}방향으로 적군을 공격합니다. [공격력 {2}]'\
            .format(self.name, location, self.damage))

class FlyingUnit:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print('{0}: {1}방향으로 날아갑니다. [속도 {2}]'\
            .format(name, location, self.flying_speed))
        
class FlyingAttackUnit(AttackUnit, FlyingUnit): # 다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        FlyingUnit.__init__(self, flying_speed)
    def move(self, location): # 메소드 오버라이딩
        self.fly(self.name, location)

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super: self 필요X, 다중상속 시 마지막 클래스만 호출
        self.location = location


# supplydepot = BuildingUnit('서플라이 디폿', 500, '7시')

# firebat1 = AttackUnit('파이어뱃', 50, 0, 16)
# firebat1.attack('5시')
# firebat1.damaged(25)
# firebat1.damaged(25)

# valkyrie = FlyingAttackUnit('발키리', 200, 6, 5)
# valkyrie.fly(valkyrie.name, '3시')

# vulture = AttackUnit('벌쳐', 80, 10, 20)
# battlecruiser = FlyingAttackUnit('배틀크루저', 500, 25, 3)
# vulture.move('11시')
# # battlecruiser.fly(battlecruiser.name, '9시')
# battlecruiser.move('9시')


# EXAMPLE
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, '마린', 40, 1, 5)
    def set_stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print('{0}: 스팀팩을 사용합니다. (hp 10 감소)' .format(self.name))
        else:
            print('{0}: 체력이 부족하여 스팀팩을 사용하지 않습니다.' .format(self.name))

class Tank(AttackUnit):
    mode = False
    def __init__(self):
        AttackUnit.__init__(self, '탱크', 150, 1, 35)
        self.mode_seize = False
    def set_seize(self):
        if Tank.mode == False:
            return
        if self.mode_seize == False: # 시즈모드 X -> 시즈모드
            print('{0}: 시즈모드로 전환합니다.')
            self.damage *= 2
            self.mode_seize = True
        else: # 시즈모드 -> 시즈모드 해제
            print('{0}: 시즈모드를 해제합ㄷ니다.')
            self.damage /= 2
            self.mode_seize = False

class Wraith(FlyingAttackUnit):
    def __init__(self):
        FlyingAttackUnit.__init__(self, '레이스', 80, 20, 5)
        self.mode_clock = False
    def set_clock(self):
        if self.mode_clock == True: # 클로킹모드 -> 클로킹모드 해제
            print('{0}: 클로킹모드를 해제합니다.' .format(self.name))
            self.mode_clock = False
        else: # 클로킹모드 X  -> 클로킹모드
            print('{0}: 클로킹모드로 전환합니다.' .format(self.name))
            self.mode_clock = True

def game_start():
    print('[새로운 게임을 시작합니다.]')

def game_over():
    print('[gg]')


game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()
t1 = Tank()
t2 = Tank()
w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move('1시')

Tank.seizemode_developed = True
print('[탱크를 시즈모드로 전환합니다.]')

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.set_stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize()
    elif isinstance(unit, Wraith):
        unit.set_clock()

for unit in attack_units:
    unit.attack('1시')

from random import *
for unit in attack_units:
    unit.damaged(randint(5, 21))

game_over()


# QUIZ
class House:
    def __init__(self, location, house_type, deal_type, price, year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.year = year
    
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.year)

houses = []

house1 = House('강남', '아파트', '매매', '10억', '2010년')
house2 = House('마포', '오피스텔', '전세', '4억', '2007년')
house3 = House('송파', '빌라', '월세', '500/100', '2000년')

houses.append(house1)
houses.append(house2)
houses.append(house3)

for house in houses:
    house.show_detail()

print('총 {0}개의 매물이 있습니다.' .format(len(houses)))