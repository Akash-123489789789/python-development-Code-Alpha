# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 20:49:42 2023

@author: User
"""

import ccxt
import time

# Initialize the Binance API
binance = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET_KEY',
})

# Define your trading parameters
symbol = 'BTC/USDT'
buy_amount = 0.001  # Amount of BTC to buy
sell_amount = 0.001  # Amount of BTC to sell
profit_margin = 1.02  # Sell when the price increases by 2%

def get_balance():
    # Get account balance
    balance = binance.fetch_balance()
    return balance['total']['USDT']

def place_buy_order(amount):
    # Place a buy order
    order = binance.create_limit_buy_order(symbol, amount, 10000)  # Replace 10000 with your desired buy price
    return order['info']['orderId']

def place_sell_order(amount):
    # Place a sell order
    order = binance.create_limit_sell_order(symbol, amount, 10000 * profit_margin)  # Replace 10000 with your desired sell price
    return order['info']['orderId']

def main():
    while True:
        try:
            # Get the current price
            ticker = binance.fetch_ticker(symbol)
            current_price = ticker['last']

            # Check if it's a good time to buy
            if get_balance() > 10:  # Check if you have enough USDT
                order_id = place_buy_order(buy_amount)
                print(f'Buy order placed. Order ID: {order_id}')

            # Check if it's a good time to sell
            elif get_balance() > 0 and current_price > 10000 * profit_margin:  # Replace 10000 with your desired sell threshold
                order_id = place_sell_order(sell_amount)
                print(f'Sell order placed. Order ID: {order_id}')

            # Wait for the next iteration
            time.sleep(60)  # Adjust the interval as needed

        except Exception as e:
            print(f'An error occurred: {str(e)}')

if __name__ == '__main__':
    main()
