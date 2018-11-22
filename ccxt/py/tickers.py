from collections import defaultdict
import ccxt

exchanges = ['binance', 'bitfinex', 'coinbase', 'ethfinex', 'kraken', 'poloniex']

# ------------------------------------------------------------------------------
'''
Approach 1

- list of lists, each inside list has the tickers for their respective exchange
- dict that has a key for each ticker, and count of the ticker across exchanges

'''

all_tickers = []

for exchange in exchanges:
	exchange = getattr(ccxt, exchange)()
	markets = exchange.fetch_markets()
	all_tickers.append([ticker['symbol'] for ticker in markets])

ticker_count = {}
for exchange_tickers in all_tickers:
	for ticker in exchange_tickers:
		if ticker in ticker_count.keys():
			ticker_count[ticker] += 1
		else:
			ticker_count[ticker] = 1


arb_pairs = [key for key, val in ticker_count.items() if val > 1]

# ------------------------------------------------------------------------------
'''
Approach 2

- dict that has the exchange as the key, and the exchange's ticker list for values
- single list that has the ticker from each exchange
- use count of the occurence of each ticker to determine arbitrage pairs

'''


exchange_pairs = defaultdict(list)
all_tickers = []

for exchange in exchanges:
	markets = getattr(ccxt, exchange)().fetch_markets()
	tickers = [ticker['symbol'] for ticker in markets]
	exchange_pairs[exchange] = tickers
	all_tickers += tickers

all_tickers.count(all_tickers[0])
