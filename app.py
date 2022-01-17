import ccxt
markets = ccxt.exchanges
for market in markets:
    w = getattr(ccxt, market)()
    try:
        m= w.fetch_ohlcv(symbol='BTC/USDT', timeframe='4h')
        if m[-2][4] < 10000:
            continue
        print(market, m[-2][4])
    finally:
        continue
    
