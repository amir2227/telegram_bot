import ccxt

def Sort_Tuple(tup): 
      
    # getting length of list of tuples
    lst = len(tup) 
    for i in range(0, lst): 
          
        for j in range(0, lst-i-1): 
            if (tup[j][1] > tup[j + 1][1]): 
                temp = tup[j] 
                tup[j]= tup[j + 1] 
                tup[j + 1]= temp 
    return tup


markets = ccxt.exchanges
market_price = []
for market in markets:
    w = getattr(ccxt, market)()
    try:
        m= w.fetch_ohlcv(symbol='BTC/USDT', timeframe='4h')
        if m[-2][4] < 10000:
            continue
        market_price.append((market, m[-2][4]))
    finally:
        continue
    
sorted_market = Sort_Tuple(market_price)
print(sorted_market)
print(sorted_market[0], sorted_market[-1])
