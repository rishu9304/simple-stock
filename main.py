import sys
import time
from utils import SimpleStockMarket

STOCK_SYMBOL = ["TEA", "POP", "ALE", "GIN", "JOE"]


def simple_stock_market():
    while True:
        option = input("Please enter your choice.\n"
                       "1. Calculate Dividend.\n"
                       "2. Calculate P/E ration.\n"
                       "3. Create Record for stock.\n"
                       "4. Calculate Volume Weighted Stock Price Within 5 Minutes.\n"
                       "5. Calculate Share Index for all the stock.\n"
                       "6. Exit From Simple Stock Market.\n")
        if option == '1':
            try:
                print("Welcome to Dividend Calculation..")
                symbol = input("Please Enter Stock From The Below Options" +
                               "\n TEA " +
                               "\n POP " +
                               "\n ALE " +
                               "\n GIN " +
                               "\n JOE \n")
                if symbol not in STOCK_SYMBOL:
                    print("Please Enter Stock From Given Options.")
                    continue
                price = input("Please Enter Price..\n")
                SimpleStockMarket.calculate_dividend(price, symbol)
            except Exception as e:
                print(f"Something wrong happen due to {str(e)}")

        elif option == '2':
            try:
                print("Welcome To P/E Ratio Calculation..")
                symbol = input("Please Enter Stock From The Below Options" +
                               "\n TEA " +
                               "\n POP " +
                               "\n ALE " +
                               "\n GIN " +
                               "\n JOE \n")
                if symbol not in STOCK_SYMBOL:
                    print("Please Enter Stock From Given Options.")
                    continue
                price = input("Please Enter Price..\n")
                SimpleStockMarket().pe_ratio(price, symbol)
            except Exception as e:
                print(f"Something wrong happen due to {str(e)}")

        elif option == '3':
            print("Welcome To Create Record For Stock..")
            quantity = input("Please Enter Quantity: ")
            action = input("Please enter action Buy/Sale For Stock: ")
            price = input("Please Enter Price: ")
            try:
                if float(price) == 0.0:
                    print("Please Enter Valid Price")
                    continue
                elif action not in ["Buy", "Sale"]:
                    print("Please Enter Valid Action")
                    continue
                SimpleStockMarket.create_record(str(time.time()), quantity, action, price)
            except Exception as e:
                print(f"Something wrong happen due to {str(e)}")

        elif option == '4':
            try:
                print("Weighted Stock Within 5 Minutes.")
                SimpleStockMarket.weighted_stock_within_five_minutes()
            except Exception as e:
                print(f"Something wrong happen due to {str(e)}")

        elif option == '5':
            try:
                print("Calculate Share Index For All Stock")
                SimpleStockMarket.geometry_mean_of_share_index()
            except Exception as e:
                print(f"Something wrong happen due to {str(e)}")

        if option == "6":
            print("Good Bye..")
            sys.exit(0)


if __name__ == "__main__":
    simple_stock_market()
