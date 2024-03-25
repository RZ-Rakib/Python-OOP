from coin_acceptor import CoinAcceptor

class Main:
    def __init__(self) -> None:
        print("Program starting.")

        # instance of CoinAcceptor, no value is initialized due to using default value
        coin_calculation = CoinAcceptor()

        # while loop to run the program continously
        while True:
            print("1 - Insert coin")
            print("2 - Show coins")
            print("3 - Return coins")
            print("0 - Exit program")

            user_selection = input("Your choice: ")

            if user_selection == "1":
                coin_calculation.insertCoin()
                print("")
            elif user_selection == "2":
                print(f"Currently '{coin_calculation.getAmount()}' coins in coin acceptor\n")
            elif user_selection == "3":
                print(f"Coin acceptor returned '{coin_calculation.returnCoins()}' coins.\n")
            elif user_selection == "0":
                print("Program ending.")
                break
            else:
                print("Invalid output, try again with a valid number.\n")

if __name__ == "__main__":
    app = Main()