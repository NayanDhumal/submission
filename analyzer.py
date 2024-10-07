import heapq

class Stock:
    def __init__(self, symbol, performance):
        self.symbol = symbol
        self.performance = performance

    def __lt__(self, other):
        return self.performance < other.performance

class RealTimeFinancialMarketAnalyzer:
    def __init__(self, top_n):
        self.top_n = top_n
        self.stock_dict = {}  # Dictionary to store stock symbol and performance

    def add_or_update_stock(self, stock):
        """
        Add or update stock in the stock dictionary. If the stock is already in the list,
        update its performance. If it's a new stock and we have less than top_n, add it.
        """
        self.stock_dict[stock.symbol] = stock.performance

    def get_top_stocks(self):
        """
        Return the top 'n' distinct stocks based on performance.
        """
        top_stocks = heapq.nlargest(self.top_n, self.stock_dict.items(), key=lambda x: x[1])
        return [Stock(symbol, performance) for symbol, performance in top_stocks]




# import heapq

# class Stock:
#     def __init__(self, symbol, performance):
#         self.symbol = symbol
#         self.performance = performance

#     def __lt__(self, other):
#         return self.performance < other.performance

# class RealTimeFinancialMarketAnalyzer:
#     def __init__(self, top_n):
#         self.top_n = top_n
#         self.min_heap = []

#     def add_stock(self, stock):
#         if len(self.min_heap) < self.top_n:
#             heapq.heappush(self.min_heap, stock)
#         else:
#             if stock.performance > self.min_heap[0].performance:
#                 heapq.heappushpop(self.min_heap, stock)

#     def get_top_stocks(self):
#         return sorted(self.min_heap, key=lambda x: -x.performance)
