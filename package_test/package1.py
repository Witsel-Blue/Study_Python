class Package1:
    def detail(self):
        print('test1')

if __name__ == '__main__':
    print('package1 모듈을 직접실행')
else:
    print('package1 외부에서 모듈 호출')