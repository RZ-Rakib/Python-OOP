class CoinAcceptor:
    __amount = int
    __value = float
    def __init__(self) -> None:
        self.__amount = 0
        self.__value = 0.0

    def insertCoin(self) -> None:
        self.__amount += 1
    
    def getAmount(self) -> int:
        return self.__amount

    def returnCoins(self) -> int:
        coins_return = self.__amount
        self.__amount = 0
        return coins_return