#execute file daily with append_data to update all the files
#comment out append_data and the system will submit orders
#same with using sudo -u ubuntu /home/ubuntu/data5500_mycode/run_final_project.sh

import json
import requests
import numpy as np
import os
from dotenv import load_dotenv
import time

try:
    from alpaca.trading.client import TradingClient
    from alpaca.trading.requests import MarketOrderRequest
    from alpaca.trading.enums import OrderSide, TimeInForce
except ImportError:
    print("Error: 'alpaca-py' module not found. Please install it in a virtual environment:")
    print("  python3 -m venv ~/trading_env")
    print("  source ~/trading_env/bin/activate")
    print("  pip install alpaca-py requests numpy python-dotenv")
    exit(1)

# Initialize results dictionary
results = {}
ordered_tickers = set()

# Load environment variables
dotenv_path = os.getenv('DOTENV_PATH', '/home/ubuntu/data5500_mycode/final_project/.env')
print(f"Attempting to load .env file from: {dotenv_path}")
if not os.path.exists(dotenv_path):
    print(f"Error: .env file not found at {dotenv_path}")
    exit(1)
loaded = load_dotenv(dotenv_path)
print(f"load_dotenv returned: {loaded}")
api_key = os.getenv('ALPACA_API_KEY')
secret_key = os.getenv('ALPACA_SECRET_KEY')
print(f"ALPACA_API_KEY: {api_key}")
print(f"ALPACA_SECRET_KEY: {secret_key}")
if not api_key or not secret_key:
    print("Error: ALPACA_API_KEY and ALPACA_SECRET_KEY must be set in a .env file.")
    print("Get new keys from https://alpaca.markets/ (Paper Trading > API Keys).")
    print("Create a .env file with:")
    print("ALPACA_API_KEY=your_new_key")
    print("ALPACA_SECRET_KEY=your_new_secret")
    exit(1)

# Verify data directory
data_dir = "/home/ubuntu/data5500_mycode/final_project/data"
if not os.path.exists(data_dir):
    try:
        os.makedirs(data_dir)
        print(f"Created directory: {data_dir}")
    except Exception as e:
        print(f"Error creating directory {data_dir}: {e}")
        exit(1)

# Alpaca API setup
try:
    trading_client = TradingClient(api_key, secret_key, paper=True)
    account = trading_client.get_account()
    print(f"Alpaca account details: {account}")
    print("Successfully connected to Alpaca API in paper trading mode")
except Exception as e:
    print(f"Error connecting to Alpaca API: {e}")
    exit(1)

# First data pull
tickers = ['AAPL', 'META', 'TSLA', 'ADBE', 'NVDA', 'TQQQ', 'COST', 'ALB', 'SLB', 'AMZN']

def first_data_pull(tickers):
    for ticker in tickers:
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+ticker+"&outputsize=full&apikey=HJXZZH5XET6YARPA"
        for attempt in range(3):
            try:
                request = requests.get(url)
                request_dictionary = json.loads(request.text)
                if "Time Series (Daily)" not in request_dictionary:
                    error_msg = request_dictionary.get('Note', 'No data')
                    print(f"Error fetching data for {ticker}: {error_msg}")
                    if "rate limit" in error_msg.lower():
                        print("Rate limit hit, retrying after delay...")
                        time.sleep(60)
                        continue
                    break
                break
            except Exception as e:
                print(f"Error fetching data for {ticker}: {e}")
                break
        else:
            print(f"Failed to fetch data for {ticker} after 3 attempts")
            continue
        
        print(round(float(request_dictionary["Time Series (Daily)"]["2024-04-10"]["4. close"]), 2))
        key1 = "Time Series (Daily)"
        file_lines = []
        close_key = "4. close"
        with open(f"{data_dir}/{ticker}.csv", "w") as file:
            for date in request_dictionary[key1].keys():
                file_lines.append(date + ", "+str(round(float(request_dictionary[key1][date][close_key]), 2))+"\n")
            file_lines.reverse()
            file.writelines(file_lines)
        time.sleep(60)
    
    return

def append_data(tickers):
    for ticker in tickers:
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+ticker+"&outputsize=full&apikey=HJXZZH5XET6YARPA"
        for attempt in range(3):
            try:
                request = requests.get(url)
                request_dictionary = json.loads(request.text)
                if "Time Series (Daily)" not in request_dictionary:
                    error_msg = request_dictionary.get('Note', 'No data')
                    print(f"Error fetching data for {ticker}: {error_msg}")
                    if "rate limit" in error_msg.lower():
                        print("Rate limit hit, retrying after delay...")
                        time.sleep(60)
                        continue
                    break
                break
            except Exception as e:
                print(f"Error fetching data for {ticker}: {e}")
                break
        else:
            print(f"Failed to fetch data for {ticker} after 3 attempts")
            continue
        
        key1 = "Time Series (Daily)"
        close_key = "4. close"
        csv_file = open(f"{data_dir}/{ticker}.csv", "r")
        csv_lines = csv_file.readlines()
        csv_file.close()
        
        latest_date = csv_lines[-1].split(",")[0]
        
        new_lines = []
        for date in request_dictionary[key1].keys():
            if date == latest_date:
                break
            new_lines.append(date + ", " + str(round(float(request_dictionary["Time Series (Daily)"][date]["4. close"]), 2)) + "\n")
            
        new_lines = new_lines[::-1]
        file = open(f"{data_dir}/{ticker}.csv", "a")
        file.writelines(new_lines)
        file.close()
    
        file_lines = []
        with open(f"{data_dir}/{ticker}.csv", "w") as file:
            for date in request_dictionary[key1].keys():
                file_lines.append(date + ", "+str(round(float(request_dictionary[key1][date][close_key]), 2))+"\n")
            file_lines = file_lines[::-1]
            file.writelines(file_lines)
        time.sleep(30)
            
    return

def get_position(ticker):
    """Check the current position for a ticker. Returns qty (positive for long, negative for short, 0 for no position)."""
    try:
        position = trading_client.get_position_by_symbol(ticker)
        qty = float(position.qty)
        return qty if position.side == 'long' else -qty
    except Exception as e:
        # If no position exists, Alpaca raises an exception
        return 0

def has_open_orders(ticker):
    """Check if there are open orders for a ticker. Returns True if open orders exist, False otherwise."""
    try:
        orders = trading_client.get_orders()
        for order in orders:
            if order.symbol == ticker and order.status not in ['filled', 'canceled', 'expired', 'rejected']:
                return True
        return False
    except Exception as e:
        print(f"Error checking open orders for {ticker}: {e}")
        return False

def submit_alpaca_order(ticker, qty, side, action):
    try:
        # Check current position
        current_position = get_position(ticker)
        has_orders = has_open_orders(ticker)
        
        # Define the intended position change
        if action == "buy":
            intended_change = qty  # Increase long position or reduce short position
        elif action == "sell":
            intended_change = -qty  # Reduce long position or increase short position
        elif action == "short sell":
            intended_change = -qty  # Increase short position
        elif action == "cover short":
            intended_change = qty  # Reduce short position
        else:
            print(f"Invalid action {action} for {ticker}")
            return

        # Check for conflicting orders or positions
        if has_orders:
            print(f"Skipping {action} order for {ticker}: An open order already exists")
            return
        
        if action == "buy":
            if current_position < 0:
                # If short, a buy order will cover the short (reduce negative position)
                if abs(current_position) < qty:
                    print(f"Skipping buy order for {ticker}: Cannot buy {qty} shares while short {abs(current_position)} shares")
                    return
            elif current_position > 0:
                print(f"Skipping buy order for {ticker}: Already long {current_position} shares")
                return
        elif action == "sell":
            if current_position <= 0:
                print(f"Skipping sell order for {ticker}: No long position to sell (current position: {current_position})")
                return
            if current_position < qty:
                print(f"Skipping sell order for {ticker}: Insufficient long shares (have {current_position}, need {qty})")
                return
        elif action == "short sell":
            if current_position > 0:
                print(f"Skipping short sell order for {ticker}: Already long {current_position} shares")
                return
            if current_position < 0:
                print(f"Skipping short sell order for {ticker}: Already short {abs(current_position)} shares")
                return
        elif action == "cover short":
            if current_position >= 0:
                print(f"Skipping cover short order for {ticker}: No short position to cover (current position: {current_position})")
                return
            if abs(current_position) < qty:
                print(f"Skipping cover short order for {ticker}: Insufficient short shares to cover (short {abs(current_position)}, need {qty})")
                return

        # Submit the order
        order_data = MarketOrderRequest(
            symbol=ticker,
            qty=qty,
            side=side,
            time_in_force=TimeInForce.DAY
        )
        order = trading_client.submit_order(order_data=order_data)
        print(f"Submitted {action} order for {ticker}: {order.id}")
    except Exception as e:
        print(f"Error submitting {action} order for {ticker}: {e}")

def meanReversion(prices, ticker):
    prices = np.array(prices)
    if len(prices) < 50:  # Need at least 50 days for 50-day MA
        print(f"Not enough data for {ticker} (need 50 days, have {len(prices)})")
        return 0, 0
    
    # Precompute moving averages
    ma_10 = np.round(np.convolve(prices, np.ones(10)/10, mode='valid'), 2)
    ma_20 = np.round(np.convolve(prices, np.ones(20)/20, mode='valid'), 2)
    ma_50 = np.round(np.convolve(prices, np.ones(50)/50, mode='valid'), 2)
    
    buy = 0
    short = 0
    first_trade = 0
    total_profit = 0
    
    for i in range(len(ma_50)):
        price = round(prices[i + 49], 2)
        avg_10 = ma_10[i + 40]
        avg_20 = ma_20[i + 30]
        avg_50 = ma_50[i]
        is_uptrend = avg_20 > avg_50
        
        if price < avg_10 * 0.95 and buy == 0 and short == 0:
            buy = price
            if i == len(ma_50) - 1 and ticker not in ordered_tickers:
                print(f"Mean Reversion strategy suggests you buy {ticker} today at ${buy}")
                submit_alpaca_order(ticker, 1, OrderSide.BUY, "buy")
                ordered_tickers.add(ticker)
            if first_trade == 0:
                first_trade = buy
        
        elif price > avg_10 * 1.05 and buy != 0:
            sell = price
            if i == len(ma_50) - 1 and ticker not in ordered_tickers:
                print(f"Mean Reversion strategy suggests you sell {ticker} today at ${sell}")
                submit_alpaca_order(ticker, 1, OrderSide.SELL, "sell")
                ordered_tickers.add(ticker)
            total_profit += round(sell - buy, 2)
            buy = 0
        
        elif price > avg_10 * 1.05 and short == 0 and buy == 0 and not is_uptrend:
            short = price
            if i == len(ma_50) - 1 and ticker not in ordered_tickers:
                print(f"Mean Reversion strategy suggests you short sell {ticker} today at ${short}")
                submit_alpaca_order(ticker, 1, OrderSide.SELL, "short sell")
                ordered_tickers.add(ticker)
            if first_trade == 0:
                first_trade = short
        
        elif price < avg_10 * 0.95 and short != 0:
            cover = price
            if i == len(ma_50) - 1 and ticker not in ordered_tickers:
                print(f"Mean Reversion strategy suggests you cover short {ticker} today at ${cover}")
                submit_alpaca_order(ticker, 1, OrderSide.BUY, "cover short")
                ordered_tickers.add(ticker)
            total_profit += round(short - cover, 2)
            short = 0
    
    returns = round((total_profit/first_trade)*100, 2) if first_trade != 0 else 0
    return total_profit, returns

def simpleMovingAverageStrategy(prices, ticker):
    prices = np.array(prices)
    if len(prices) < 20:
        print(f"Not enough data for {ticker} (need 20 days, have {len(prices)})")
        return 0, 0
    
    window = 20
    sma = np.round(np.convolve(prices, np.ones(window)/window, mode='valid'), 2)
    
    buy = 0
    short = 0
    first_trade = 0
    total_profit = 0
    
    for i in range(len(sma)):
        price = round(prices[i + window - 1], 2)
        avg = sma[i]
        
        if price > avg and buy == 0 and short == 0:
            buy = price
            if i == len(sma) - 1 and ticker not in ordered_tickers:
                print(f"Simple Moving Average strategy suggests you buy {ticker} today at ${buy}")
                submit_alpaca_order(ticker, 1, OrderSide.BUY, "buy")
                ordered_tickers.add(ticker)
            if first_trade == 0:
                first_trade = buy
        elif price < avg and buy != 0:
            sell = price
            total_profit += round(sell - buy, 2)
            if i == len(sma) - 1 and ticker not in ordered_tickers:
                print(f"Simple Moving Average strategy suggests you sell {ticker} today at ${sell}")
                submit_alpaca_order(ticker, 1, OrderSide.SELL, "sell")
                ordered_tickers.add(ticker)
            buy = 0
        elif price < avg and short == 0 and buy == 0:
            short = price
            if i == len(sma) - 1 and ticker not in ordered_tickers:
                print(f"Simple Moving Average strategy suggests you short sell {ticker} today at ${short}")
                submit_alpaca_order(ticker, 1, OrderSide.SELL, "short sell")
                ordered_tickers.add(ticker)
            if first_trade == 0:
                first_trade = short
        elif price > avg and short != 0:
            cover = price
            total_profit += round(short - cover, 2)
            if i == len(sma) - 1 and ticker not in ordered_tickers:
                print(f"Simple Moving Average strategy suggests you cover short {ticker} today at ${cover}")
                submit_alpaca_order(ticker, 1, OrderSide.BUY, "cover short")
                ordered_tickers.add(ticker)
            short = 0
    
    returns = round((total_profit/first_trade)*100, 2) if first_trade != 0 else 0
    return total_profit, returns

def bollingerBands(prices, ticker):
    prices = np.array(prices)
    if len(prices) < 10:
        print(f"Not enough data for {ticker} (need 10 days, have {len(prices)})")
        return 0, 0
    
    window = 10
    ma = np.round(np.convolve(prices, np.ones(window)/window, mode='valid'), 2)
    std = np.zeros(len(ma))
    for i in range(len(ma)):
        std[i] = np.std(prices[i:i+window])
    std = np.round(std, 2)
    high_band = ma + 2 * std
    low_band = ma - 2 * std
    
    buy = 0
    short = 0
    first_trade = 0
    total_profit = 0
    
    for i in range(len(ma)):
        price = round(prices[i + window - 1], 2)
        avg = ma[i]
        upper = high_band[i]
        lower = low_band[i]
        
        if price < lower and buy == 0 and short == 0:
            buy = price
            if i == len(ma) - 1 and ticker not in ordered_tickers:
                print(f"Bollinger Bands strategy suggests you buy {ticker} today at ${buy}")
                submit_alpaca_order(ticker, 1, OrderSide.BUY, "buy")
                ordered_tickers.add(ticker)
            if first_trade == 0:
                first_trade = buy
        elif price > avg and buy != 0:
            sell = price
            if i == len(ma) - 1 and ticker not in ordered_tickers:
                print(f"Bollinger Bands strategy suggests you sell {ticker} today at ${sell}")
                submit_alpaca_order(ticker, 1, OrderSide.SELL, "sell")
                ordered_tickers.add(ticker)
            total_profit += round(sell - buy, 2)
            buy = 0
        elif price > upper and short == 0 and buy == 0:
            short = price
            if i == len(ma) - 1 and ticker not in ordered_tickers:
                print(f"Bollinger Bands strategy suggests you short sell {ticker} today at ${short}")
                submit_alpaca_order(ticker, 1, OrderSide.SELL, "short sell")
                ordered_tickers.add(ticker)
            if first_trade == 0:
                first_trade = short
        elif price < avg and short != 0:
            cover = price
            if i == len(ma) - 1 and ticker not in ordered_tickers:
                print(f"Bollinger Bands strategy suggests you cover short {ticker} today at ${cover}")
                submit_alpaca_order(ticker, 1, OrderSide.BUY, "cover short")
                ordered_tickers.add(ticker)
            total_profit += round(short - cover, 2)
            short = 0
    
    returns = round((total_profit/first_trade)*100, 2) if first_trade != 0 else 0
    return total_profit, returns 
 
  
def saveresults(dictionary):
    json.dump(dictionary, open(f"{data_dir}/results.json", "w"), indent=4)

def main():
    #append_data(tickers)  # Update data
    global ordered_tickers
    ordered_tickers = set()  # Reset ordered tickers for this run
    highest_profit = 0
    best_ticker = ""
    best_strategy = ""
    
    for ticker in tickers:
        try:
            file = open(f"{data_dir}/{ticker}.csv", "r")
            prices = [float(round(float(line.split(",")[1].strip()), 2)) for line in file.readlines()]
            file.close()
        except Exception as e:
            print(f"Error reading CSV for {ticker}: {e}")
            continue

        mr_profit, mr_returns = meanReversion(prices, ticker)
        sa_profit, sa_returns = simpleMovingAverageStrategy(prices, ticker)
        bb_profit, bb_returns = bollingerBands(prices, ticker)
        
        results[ticker+"_prices"] = [round(p, 2) for p in prices]
        results[ticker+"_mr_profit"] = round(mr_profit, 2)
        results[ticker+"_mr_returns"] = round(mr_returns, 2)
        results[ticker+"_sa_profit"] = round(sa_profit, 2)
        results[ticker+"_sa_returns"] = round(sa_returns, 2)
        results[ticker+"_bb_profit"] = round(bb_profit, 2)
        results[ticker+"_bb_returns"] = round(bb_returns, 2)
        
        saveresults(results)
        
        if mr_profit > highest_profit:
            highest_profit = round(mr_profit, 2)
            best_ticker = ticker
            best_strategy = "Mean Reversion"
        elif sa_profit > highest_profit:
            highest_profit = round(sa_profit, 2)
            best_ticker = ticker
            best_strategy = "Simple Moving Average"
        elif bb_profit > highest_profit:
            highest_profit = round(bb_profit, 2)
            best_ticker = ticker
            best_strategy = "Bollinger Bands"
            
    results["highest_profit"] = round(highest_profit, 2)
    results["best_ticker"] = best_ticker
    results["best_strategy"] = best_strategy
    
    print(f"The ticker that earned the most profit was {best_ticker} which earned a profit of ${highest_profit} using {best_strategy} strategy!")

if __name__ == "__main__":
    main()
