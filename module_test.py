def price(people):
    print('{0}명 {1}원' .format(people, people * 10000))

def price_morning(people):
    print('{0}명 {1}원(조조할인)' .format(people, people * 6000))

def price_soldier(people):
    print('{0}명 {1}원(군인할인)' .format(people, people * 4000))