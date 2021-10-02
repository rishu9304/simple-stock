# Stock Price System
# Contributor: Rishabh Kumar (agarahari110@gmail.com)
import time

import pandas as pd

# read csv file into pandas dataframe
GBCE_df = pd.read_csv('stock.csv')

# getting all the stock symbols in dictionary
stock_symbols_list = GBCE_df["stock_symbol"].to_list()


class SimpleStockMarket:

    # calculate the dividend yield based on user price input
    @staticmethod
    def calculate_dividend(price, stock_symbol):

        if stock_symbol not in stock_symbols_list:
            print("The stock which you have entered does not exits please try with valid..")

        # getting the entire row the particular stock symbol
        stock_row_df = GBCE_df[GBCE_df['stock_symbol'] == stock_symbol]
        if stock_row_df.iloc[0, 1] == "Common":
            try:
                last_dividend = stock_row_df.iloc[0, 2]
                # calculated based on the formula
                dividend_yield = float(last_dividend)/float(price)
                print("Dividend yield:", dividend_yield)
                return True
            except Exception as e:
                print(f"Something wrong happen due to {str(e)}")
                return False
        else:
            try:
                last_dividend = stock_row_df.iloc[0, 2]
                per_value = stock_row_df.iloc[0, 4]
                # calculated based on the formula
                dividend_yield = (float(last_dividend) * float(per_value))/float(price)
                print("Dividend yield:", dividend_yield)
                return True
            except Exception as e:
                print(f"Something wrong happen due to {str(e)}")
                return False

    # Calculate the P/E Ratio
    def pe_ratio(self, price, stock_symbol):
        try:
            dividend = self.calculate_dividend(price, stock_symbol)
            if dividend == 0.0:
                return False
            else:
                pe_ratio = float(price)/dividend
                print("P/E ratio:", pe_ratio)
                return True
        except Exception as e:
            print(f"Something wrong happen due to {str(e)}")
            return False

    # Record trade based on input
    @staticmethod
    def create_record(timestamp, quantity, action, price):
        # open file in append mode for create record for trade
        try:
            with open('record_trade.txt', 'a') as file:
                file.write(timestamp + "," + quantity + "," + action + "," + price + "\n")
                print("Successfully added all the following details")
                print("timestamp:", timestamp, "quantity:", quantity, "action:", action, "price:", price)
            return True
        except Exception as e:
            print(f"Something wrong happen due to {str(e)}")
            return False

    @staticmethod
    def weighted_stock_within_five_minutes():
        # calculate volume weighted stock price within 5 minutes
        try:
            # open record trade file in read mode
            sum_of_quantity = 0
            sum_of_price_quantity = 0
            with open("record_trade.txt", 'r') as file:
                for line in file:
                    line_list = line.split(",")
                    timestamp = float(line_list[0])
                    # consider record created within 5 minutes
                    if (time.time() - timestamp)/60 <= 5:
                        sum_of_price_quantity += float(line_list[1]) * float(line_list[3])
                        sum_of_quantity += float(line_list[1])
                if sum_of_quantity == 0:
                    print("No trade within 5 minutes of interval")
                    return False
                weight_stock = sum_of_price_quantity/sum_of_quantity
                print("Weighted stock withing 5 minutes:", weight_stock)
                return True
        except Exception as e:
            print(f"Something wrong happen due to {str(e)}")

    @staticmethod
    def geometry_mean_of_share_index():
        # calculate the geometry mean of share index for all the stocks
        try:
            # open record trade file in read mode
            sum_of_quantity = 0
            sum_of_price_quantity = 0
            with open("record_trade.txt", 'r') as file:
                for line in file:
                    line_list = line.split(",")
                    sum_of_price_quantity += float(line_list[1]) * float(line_list[3])
                    sum_of_quantity += float(line_list[1])
                if sum_of_quantity == 0:
                    print("No trade record..")
                    return True
                else:
                    share_index = sum_of_price_quantity ** 1/sum_of_quantity
                    print("Geometric mean for share index:", share_index)
                    return True
        except Exception as e:
            print(f"Something wrong happen due to {str(e)}")
            return False
