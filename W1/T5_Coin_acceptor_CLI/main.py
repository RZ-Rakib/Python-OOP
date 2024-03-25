from coin_acceptor_CLI import CoinAcceptor

class Main:
    def __init__(self) -> None:
        print("Program starting.")
        print("Welcome to coin acceptor program.")
        print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)\n")

        # instance of CoinAcceptor, no value is initialized due to using default value
        coin_calculation = CoinAcceptor()

        # while loop to run the program continously
        while True:
            user_selection = float(input("Insert coin(0 return, -1 exit): "))

            try:
                if user_selection == -1:
                    print("Exiting program.\n")
                    print("Program ending.")
                    break
                elif user_selection == 0:
                    coin_calculation.returnCoins()
                else:
                    coin_calculation.insertCoin(user_selection)
            except ValueError:
                print("Invalid input, please retype a valid number")

if __name__ == "__main__":
    app = Main()