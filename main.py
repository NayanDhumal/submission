from flask import Flask, render_template, jsonify
from analyzer import RealTimeFinancialMarketAnalyzer, Stock
from stock_data_simulator import generate_stock_data
import threading

app = Flask(__name__)

# Create a shared analyzer instance for tracking top 5 stocks
analyzer = RealTimeFinancialMarketAnalyzer(top_n=10)

# Background thread to keep updating the stock data
def update_stock_data():
    for symbol, performance in generate_stock_data():
        stock = Stock(symbol, performance)
        analyzer.add_or_update_stock(stock)

# Start background thread for real-time stock updates
threading.Thread(target=update_stock_data, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/top-stocks')
def top_stocks():
    top_stocks = analyzer.get_top_stocks()
    stocks = [{'symbol': stock.symbol, 'performance': stock.performance} for stock in top_stocks]
    return jsonify(stocks)

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template, jsonify
# from analyzer import RealTimeFinancialMarketAnalyzer, Stock
# from stock_data_simulator import generate_stock_data
# import threading

# app = Flask(__name__)

# # Shared analyzer instance
# analyzer = RealTimeFinancialMarketAnalyzer(top_n=5)

# # Background thread to keep updating the stock data
# def update_stock_data():
#     for symbol, performance in generate_stock_data():
#         stock = Stock(symbol, performance)
#         analyzer.add_stock(stock)

# # Start background thread for real-time data updates
# threading.Thread(target=update_stock_data, daemon=True).start()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/top-stocks')
# def top_stocks():
#     top_stocks = analyzer.get_top_stocks()
#     stocks = [{'symbol': stock.symbol, 'performance': stock.performance} for stock in top_stocks]
#     return jsonify(stocks)

# if __name__ == '__main__':
#     app.run(debug=True)

# ---------------------------------------------------------------------------------------
# from analyzer import RealTimeFinancialMarketAnalyzer, Stock
# from stock_data_simulator import generate_stock_data

# def display_top_stocks(analyzer):
#     """
#     Display the top stocks tracked by the analyzer.
#     """
#     top_stocks = analyzer.get_top_stocks()
#     print("\nTop Stocks:")
#     for stock in top_stocks:
#         print(f"{stock.symbol}: {stock.performance}")

# def main():
#     """
#     Main function to run the real-time financial market analyzer.
#     """
#     top_n = int(input("Enter the number of top-performing stocks to track: "))
#     analyzer = RealTimeFinancialMarketAnalyzer(top_n=top_n)

#     print("\nStarting real-time stock data simulation...")
#     for symbol, performance in generate_stock_data():
#         stock = Stock(symbol, performance)
#         analyzer.add_stock(stock)
#         display_top_stocks(analyzer)

# if __name__ == "__main__":
#     main()
