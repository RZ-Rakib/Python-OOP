class CoinAcceptor:
    def __init__(self) -> None:
        self.coin_counts = 0
        self.total_value = 0.0

    def insertCoin(self, value: float) -> None:
        self.coin_counts += 1
        self.total_value += value
        print("Inserting...")
        print(f"Inserted coins - {self.coin_counts}, value - {self.total_value:.1f}€\n")

    def returnCoins(self) -> tuple[int, float]:
        print("Returning coins...")
        print(f"{self.coin_counts} coins with {self.total_value}€ value returned.")
        coins_return = self.coin_counts
        inserted_value = self.total_value
        self.coin_counts = 0
        self.total_value = 0
        print(f"Inserted coins - {self.coin_counts}, value - {self.total_value}€\n")
        return coins_return, inserted_value