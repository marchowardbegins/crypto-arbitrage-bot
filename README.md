## crypto-arbitrage-bot
A bot for detecting the most profitable arbitrage opportunities across hundreds of cryptocurrency exchanges and executing instant trades.

**Requirements:**
1. List largest arbitrage opportunities, then send signal via bot
2. Execute trades automatically based on best arbitrage opportunity

**Arbitrage Strategies:**
  * Exchange Listing Strategy (New token listing on exchange): use CryptoLand for real-time listing alerts (https://itunes.apple.com/us/app/cryptoland-realtime-prices/id1321632774?mt=8%22)
  * Arbitrage Parity Trading (APT): Reporting of non-parity between trading pairs:  https://github.com/karthik947/Binance-Parity-Scanner

* Pricing Strategy:
  * Detect cryptocurrency price discrancy via Coinlib: https://arbidex.uk.com/ (the API: https://coinlib.io/apidocs)

* Geo Strategy:
  * Execute trades as close as possible to exchanges (i.e. ping time response)
  
* Centralized versus Dencentralized Exchange
  * For a possibly faster way to quickly see the crypto price differences amongst exchange (centralized and decentralized) CoinMarketCap shows the token price difference among all of the token's markets.  API to explore and test: https://pro.coinmarketcap.com/api/v1
