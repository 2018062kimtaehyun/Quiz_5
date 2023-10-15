class Bbang:
    def __init__(self, flavor, price):
        self.flavor = flavor
        self.price = int(price)
        self.total = 0

    def sell(self):
        self.total += self.price
        print(self.flavor, "맛 붕어빵을", self.price, "원에 팔았습니다.")

    def eat(self):
        print(self.flavor, "맛 붕어빵을 먹었습니다.")

bbang1 = Bbang("슈크림", 1500)

bbang2 = Bbang("팥", 1200)

bbang1.sell()
bbang2.sell()
bbang1.sell()
bbang1.eat()
bbang1.eat()
print("총 판매금액:", bbang1.total + bbang2.total)
