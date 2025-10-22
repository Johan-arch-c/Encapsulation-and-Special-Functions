class Computer:
    def __init__(self):
        self.__maxprice=9000
    def sell(self):
        print("selling price:{}".format(self.__maxprice))
    def setMaxPrice(self,price):
        self.__maxprice=price
c=Computer()
c.sell()
c.__maxprice=1000000000000000000
c.sell()
c.setMaxPrice(1000000000000000000)
c.sell()